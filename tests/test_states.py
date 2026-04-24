from demo_project.states import average1, highest1, lowest1


def teat1() -> None:
    assert average1([11, 11, 11]) == 11


def test2() -> None:
    assert highest1([11, 12, 13]) == 13


def test3() -> None:
    assert lowest1([11, 12, 13]) == 11
