from station.lib import ADefaultGroundSprite
from station.lib.registers import Registers

track_ground = ADefaultGroundSprite(1012, flags={"add": Registers.CLIMATE_RAIL_OFFSET})
road_ground_x = ADefaultGroundSprite(1314)
road_ground_y = ADefaultGroundSprite(1313)
road_ground_turn = ADefaultGroundSprite(1321)
road_ground_vanilla = ADefaultGroundSprite(1333)
default_ground = ADefaultGroundSprite(3981, flags={"add": Registers.CLIMATE_OFFSET})
slope_1_ground = ADefaultGroundSprite(3989, flags={"add": Registers.CLIMATE_OFFSET})
slope_2_ground = ADefaultGroundSprite(3990, flags={"add": Registers.CLIMATE_OFFSET})
slope_3_ground = ADefaultGroundSprite(3994, flags={"add": Registers.CLIMATE_OFFSET})
building_ground = ADefaultGroundSprite(1420, flags={"add": Registers.ZERO})
