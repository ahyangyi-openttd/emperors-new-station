from station.lib import Demo


def repeat(layouts_list, n):
    return [row * n for row in layouts_list]


def get_demos(entries):
    return {
        "Sample Layouts": [
            Demo(repeat([[entries[1]], [entries[0]], [entries[0]], [entries[2]]], 4), "Emperor's New Rail Station")
        ]
    }
