from demo_project.massage import massage1, massage2


def test1() -> None:
    assert massage1(11, "E") == "score: 11, grade: E"


def test2() -> None:
    a = massage2(count=11, average=11, highest=11, lowest=11)
    assert "you entered 11 scores" in a
    assert "average: 11" in a
    assert "highest: 11" in a
    assert "lowest: 11" in a
