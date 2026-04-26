from demo_project.storage import scores_load


def test1() -> None:
    assert scores_load == []


def test2() -> None:
    assert scores_load is None
