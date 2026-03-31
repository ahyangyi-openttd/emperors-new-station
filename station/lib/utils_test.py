from station.lib.utils import get_1cc_remap


def test_get_1cc_remap_smoke():
    result = get_1cc_remap(0)
    assert result is not None
