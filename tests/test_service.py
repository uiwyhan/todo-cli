import pytest

from demo_project.service import f, g, h


def test1() -> None:
    a = []
    b = "wuyihan"
    f(a, b)
    for i in a:
        assert i.a == 1
        assert i.b == "wuyihan"
        assert i.c == False
    assert len(a) == 1


def test2() -> None:
    a = []
    b = ""
    with pytest.raises(ValueError):
        f(a, b)


def test3() -> None:
    a = []
    f(a, "wuyihan")
    f(a, "wuyiqina")
    g(a, 1)
    for i in a:
        if i == 1:
            assert i.c == True
        elif i == 2:
            assert i.c == False


def test4() -> None:
    a = []
    b = 11
    with pytest.raises(ValueError):
        g(a, b)


def test5() -> None:
    a = []
    f(a, "wuyihan")
    f(a, "wuyiqian")
    b = h(a, 1)
    assert b.a == 1
    assert b.b == "wuyihan"
    assert b.c == False
    assert len(a) == 1


def test6() -> None:
    a = []
    b = 1111
    with pytest.raises(ValueError):
        h(a, b)
