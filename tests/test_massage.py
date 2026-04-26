from demo_project.massage import massage1, massage2


def test1() -> None:
    assert "score: 11, grade: E" in massage1(11, "E")


def test2() -> None:
    a = massage2(
        count=11,
        average=11,
        highest=11,
        lowest=11,
    )
    assert "You entered 11 scores" in a
    assert "Average: 11"
    assert "Highest: 11"
    assert "Lowest: 11"
