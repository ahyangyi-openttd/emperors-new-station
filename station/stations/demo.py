from station.lib import Demo, ALayout, ADefaultGroundSprite


def repeat(layouts_list, n):
    return [row * n for row in layouts_list]


def get_demos(entries):
    from .roadstops import layout_0, layout_1, layout_2, layout_3

    road_paved_x = ADefaultGroundSprite(1314)
    road_paved_y = ADefaultGroundSprite(1313)
    road_t_junction_e = ADefaultGroundSprite(1316)
    road_t_junction_n = ADefaultGroundSprite(1317)
    road_t_junction_w = ADefaultGroundSprite(1318)
    road_t_junction_s = ADefaultGroundSprite(1319)

    layout_road_x = ALayout(road_paved_x, [], True)
    layout_road_y = ALayout(road_paved_y, [], True)
    layout_road_t_junction_e = ALayout(road_t_junction_e, [], True)
    layout_road_t_junction_n = ALayout(road_t_junction_n, [], True)
    layout_road_t_junction_w = ALayout(road_t_junction_w, [], True)
    layout_road_t_junction_s = ALayout(road_t_junction_s, [], True)

    return {
        "Sample Layouts": [
            Demo(repeat([[entries[1]], [entries[0]], [entries[0]], [entries[1]]], 4), "Emperor's New Rail Station"),
            Demo(
                repeat([[entries[2]], [entries[0]], [entries[0]], [entries[2]]], 4), "Emperor's New Urban Rail Station"
            ),
            Demo(
                [
                    [entries[2], layout_1, entries[2], entries[2], entries[2]],
                    [entries[2], layout_road_t_junction_e, layout_road_x, layout_road_t_junction_s, layout_2],
                    [entries[2], layout_road_y, entries[2], layout_road_y, entries[2]],
                    [layout_0, layout_road_t_junction_n, layout_road_x, layout_road_t_junction_w, entries[2]],
                    [entries[2], entries[2], entries[2], layout_3, entries[2]],
                ],
                "Emperor's New Road Stop",
            ),
        ]
    }
