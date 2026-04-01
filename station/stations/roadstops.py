from agrf.lib.building.roadstop import ARoadStop
from agrf.lib.building.registers import Registers
from agrf.magic import Switch
from station.lib import ALayout, ADefaultGroundSprite
from station.lib.parameters import parameter_list
from station.stations.railway_stations import ENS_CLASS

stop_0 = ADefaultGroundSprite(2692)
stop_1 = ADefaultGroundSprite(2693)
stop_2 = ADefaultGroundSprite(2694)
stop_3 = ADefaultGroundSprite(2695)

paved_x = ADefaultGroundSprite(1314)
paved_y = ADefaultGroundSprite(1313)
bare_road_x = ADefaultGroundSprite(1333, {"add": Registers.CLIMATE_ROAD_OFFSET})
bare_road_y = ADefaultGroundSprite(1332, {"add": Registers.CLIMATE_ROAD_OFFSET})

layout_0 = ALayout(stop_0, [], True, category=ENS_CLASS)
layout_1 = ALayout(stop_1, [], True, category=ENS_CLASS)
layout_2 = ALayout(stop_2, [], True, category=ENS_CLASS)
layout_3 = ALayout(stop_3, [], True, category=ENS_CLASS)
layout_4 = ALayout(paved_x, [], True, category=ENS_CLASS)
layout_5 = ALayout(paved_y, [], True, category=ENS_CLASS)
layout_1332_4 = ALayout(bare_road_x, [], True, category=ENS_CLASS)
layout_1332_5 = ALayout(bare_road_y, [], True, category=ENS_CLASS)

switch = Switch(ranges={0: layout_0, 1: layout_1, 2: layout_2, 3: layout_3, 4: layout_4}, default=layout_5, code="view")

switch_1332 = Switch(
    ranges={0: layout_0, 1: layout_1, 2: layout_2, 3: layout_3, 4: layout_1332_4}, default=layout_1332_5, code="view"
)


def make_roadstop(roadstops, base_id, translation_name, graphics, doc_layout, general_flags=0x0):
    roadstops.append(
        ARoadStop(
            id=base_id,
            translation_name=translation_name,
            graphics=graphics,
            general_flags=general_flags,
            class_label=ENS_CLASS,
            enable_if=[parameter_list["ROADSTOP"]],
            doc_layout=doc_layout,
        )
    )
    roadstops.append(
        ARoadStop(
            id=0x80 + base_id,
            translation_name="WAYPOINT",
            graphics=graphics,
            general_flags=0x8,
            class_label=ENS_CLASS,
            enable_if=[parameter_list["ROADSTOP"]],
            doc_layout=doc_layout,
            is_waypoint=True,
        )
    )


roadstops = []
make_roadstop(roadstops, 0x01, "STOP", switch, layout_4)
make_roadstop(roadstops, 0x00, "STOP", switch_1332, layout_1332_4, general_flags=0x8)
