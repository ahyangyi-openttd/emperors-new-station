from roadstop.lib import ARoadStop
from agrf.magic import Switch
from station.lib import ALayout, ADefaultGroundSprite
from station.lib.parameters import parameter_list
from station.stations.railway_stations import ENS_CLASS

# Bus stop ground sprites for bay stops (views 0-3)
bus_stop_0 = ADefaultGroundSprite(2691)
bus_stop_1 = ADefaultGroundSprite(2692)
bus_stop_2 = ADefaultGroundSprite(2693)
bus_stop_3 = ADefaultGroundSprite(2694)

# Road paved sprites for drive-through (views 4-5)
road_paved_x = ADefaultGroundSprite(1314)
road_paved_y = ADefaultGroundSprite(1313)


layout_0 = ALayout(bus_stop_0, [], True, category=ENS_CLASS)
layout_1 = ALayout(bus_stop_1, [], True, category=ENS_CLASS)
layout_2 = ALayout(bus_stop_2, [], True, category=ENS_CLASS)
layout_3 = ALayout(bus_stop_3, [], True, category=ENS_CLASS)
layout_4 = ALayout(road_paved_x, [], True, category=ENS_CLASS)
layout_5 = ALayout(road_paved_y, [], True, category=ENS_CLASS)

switch = Switch(ranges={0: layout_0, 1: layout_1, 2: layout_2, 3: layout_3, 4: layout_4}, default=layout_5, code="view")

roadstops = [
    ARoadStop(
        id=0x00,
        translation_name="STOP",
        graphics=switch,
        general_flags=0x0,
        class_label=ENS_CLASS,
        enable_if=[parameter_list["ROADSTOP"]],
        doc_layout=layout_0,
    ),
    ARoadStop(
        id=0x80,
        translation_name="WAYPOINT",
        graphics=switch,
        general_flags=0x8,
        class_label=ENS_CLASS,
        enable_if=[parameter_list["ROADSTOP"]],
        doc_layout=layout_0,
        is_waypoint=True,
    ),
]
