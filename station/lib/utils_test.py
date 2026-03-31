from station.lib.utils import get_1cc_remap, class_label_printable


def test_class_label_printable_basic():
    # 'A' (0x41), NUL (0x00 -> '0'), space (0x20)
    data = b"A\x00 "
    assert class_label_printable(data) == "A0 "


def test_class_label_printable_mixed_controls_and_printables():
    # ESC (0x1B -> '1B'), DEL (0x7F -> '\x7f' by chr), space, 'A'
    data = bytes([0x1B, 0x7F, 0x20, 0x41])
    expected = "1B" + "\x7f" + " " + "A"
    assert class_label_printable(data) == expected


def test_get_1cc_remap_smoke():
    # Smoke test: function executes and returns a value
    result = get_1cc_remap(0)
    assert result is not None
