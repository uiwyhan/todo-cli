import pytest

from demo_project.service import TaskNotFoundError, f, g, h


def test1() -> None:
    a: list = []
    f(a, "wuyihan")
    for i in a:
        assert i.a == 1
        assert i.b == "wuyihan"
        assert not i.c


def test2() -> None:
    a = []
    f(a, "wuyihan")
    g(a, 1)
    for i in a:
        assert i.a == 1
        assert i.b == "wuyihan"
        assert i.c


def test3() -> None:
    a = []
    f(a, "wuyihan")
    b = h(a, 1)
    assert b.a == 1
    assert b.b == "wuyihan"
    assert not b.c
    assert len(a) == 0


def test_done_task_not_found() -> None:
    a = []
    b = f(a, "wuyihan")
    a.append(b)
    with pytest.raises(TaskNotFoundError):
        g(a, 1111)


def test_delete_task_not_found() -> None:
    a = []
    b = f(a, "wuyihan")
    a.append(b)
    with pytest.raises(TaskNotFoundError):
        h(a, 1111)
