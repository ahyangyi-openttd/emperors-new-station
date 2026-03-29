import types
import grf
from dataclasses import replace
from agrf.sprites import empty_alternatives
from station.lib import AStation, AMetaStation, Demo, ALayout, BuildingCylindrical, BuildingSymmetrical
from station.lib.parameters import parameter_list
from .misc import track_ground, default_ground, building_ground

ENS_CLASS = b"ENS_"
current_id = 0


def make_station(layout, symmetry, notes=None):
    global current_id
    var = symmetry.get_all_variants(layout)
    l = symmetry.create_variants(var)

    base_id = current_id
    current_id += 1

    stations = [
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
    ]

    if layout.traversable:
        wp_l = replace(l, notes=["waypoint"])
        stations.append(
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

    return stations, l


def register():
    station_tiles = []
    entries = []

    s, l = make_station(ALayout(track_ground, [], True, category=ENS_CLASS), BuildingSymmetrical)
    station_tiles.extend(s)
    entries.append(l)

    s, l = make_station(ALayout(default_ground, [], False, category=ENS_CLASS), BuildingCylindrical)
    station_tiles.extend(s)
    entries.append(l)

    s, l = make_station(ALayout(building_ground, [], False, category=ENS_CLASS), BuildingCylindrical)
    station_tiles.extend(s)
    entries.append(l)

    return station_tiles, entries


station_tiles, entries = register()


def repeat(layouts_list, n):
    return [row * n for row in layouts_list]


demos = {
    "Sample Layouts": [
        Demo(repeat([[entries[0]], [entries[0].T]], 3), "Railway station with tracks"),
        Demo(repeat([[entries[0]], [entries[0].T]], 3), "Waypoint"),
        Demo(repeat([[entries[1]] * 3], 3), "Bare land"),
        Demo(repeat([[entries[2]] * 3], 3), "Urban ground"),
    ]
}


def make_empty_variant(w, h, x, y):
    empty_image = empty_alternatives(w, h, x, y)
    empty_image.squash = types.MethodType(lambda self, *args, empty_image=empty_image: self, empty_image)
    return BuildingCylindrical.create_variants([empty_image])


empty_offset = (-31, -34)
empty_sprite = make_empty_variant(64, 68, *empty_offset)

the_stations = AMetaStation(station_tiles, ENS_CLASS, [ENS_CLASS], demos, road_stops=[])

from .roadstops import roadstops

the_stations.road_stops = roadstops
