from demo_project.storage import scores_load, scores_save


def test1() -> None:
    a = [11, 12, 13, 14]
    scores_save(a)
    c = scores_load()
    assert c == [11, 12, 13, 14]
