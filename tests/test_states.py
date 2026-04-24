from demo_project.states import get_average, get_highest, get_lowest


def test1() -> None:
    a = get_average([11, 11, 11])
    assert a == 11


def test2() -> None:
    a = get_highest([11, 11, 11])
    assert a == 11


def test3() -> None:
    a = get_lowest([11, 11, 11])
    assert a == 11
