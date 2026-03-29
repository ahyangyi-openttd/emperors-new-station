from agrf.parameters import Parameter, ParameterList
from agrf.magic import Switch
from grf import ParameterMapping

booldict = {0: "ENABLED", 1: "DISABLED"}

parameter_list = ParameterList(
    [
        Parameter(
            "RAIL_STATION",
            0,
            booldict,
            mapping=ParameterMapping(grf_parameter=0x0, first_bit=0, num_bit=1),
            option_name="BOOLEAN",
        ),
        Parameter(
            "ROADSTOP",
            0,
            booldict,
            mapping=ParameterMapping(grf_parameter=0x0, first_bit=1, num_bit=1),
            option_name="BOOLEAN",
        ),
    ]
)
