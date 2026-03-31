from dataclasses import replace
from station.lib import AStation, AMetaStation, ALayout, BuildingCylindrical, BuildingSymmetrical
from station.lib.parameters import parameter_list
from .misc import track_ground, default_ground, building_ground
from .demo import get_demos

ENS_CLASS = b"ENS_"


def make_station(station_tiles, entries, layout, symmetry, base_id, notes=None):
    var = symmetry.get_all_variants(layout)
    l = symmetry.create_variants(var)

    station_tiles.append(
        AStation(
            id=base_id,
            translation_name="RAIL_NAME",
            layouts=[l, l.M],
            class_label=ENS_CLASS,
            non_traversable_tiles=0b00 if layout.traversable else 0b11,
            is_waypoint=False,
            callbacks={"select_tile_layout": 0, "select_sprite_layout": 0},
            enable_if=[parameter_list["RAIL_STATION"]],
            doc_layout=l,
        )
    )

    if layout.traversable:
        wp_l = replace(l, notes=["waypoint"])
        station_tiles.append(
            AStation(
                id=0x80 + base_id,
                translation_name="RAIL_WAYPOINT",
                layouts=[wp_l, wp_l.M],
                class_label=ENS_CLASS,
                non_traversable_tiles=0b00,
                is_waypoint=True,
                callbacks={"select_tile_layout": 0, "select_sprite_layout": 0},
                enable_if=[parameter_list["RAIL_STATION"]],
                doc_layout=wp_l,
            )
        )

    entries.append(l)


def register():
    station_tiles = []
    entries = []

    make_station(station_tiles, entries, ALayout(track_ground, [], True, category=ENS_CLASS), BuildingSymmetrical, 0x00)
    make_station(
        station_tiles, entries, ALayout(default_ground, [], False, category=ENS_CLASS), BuildingCylindrical, 0x10
    )
    make_station(
        station_tiles, entries, ALayout(building_ground, [], False, category=ENS_CLASS), BuildingCylindrical, 0x11
    )

    return station_tiles, entries


station_tiles, entries = register()

demos = get_demos(entries)


the_stations = AMetaStation(station_tiles, ENS_CLASS, [ENS_CLASS], demos, road_stops=[])

from .roadstops import roadstops

the_stations.road_stops = roadstops
