from demo_project.cli import add_score, clear_scores, k, summary_scores
from demo_project.massage import MENU


def test1(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    a: list[int] = []
    b = add_score(a)
    c = capsys.readouterr()
    assert b is None
    assert "Invalid input. please enter a number." in c.out


def test2(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "11")
    a: list[int] = []
    b = add_score(a)
    c = capsys.readouterr()
    assert b is None
    assert "score: 11, grade: E" in c.out


def test3(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "111")
    a = []
    b = add_score(a)
    c = capsys.readouterr()
    assert b is None
    assert "Invalid input. please enter a number from 0 to 100." in c.out


def test4(capsys) -> None:
    a = []
    b = summary_scores(a)
    c = capsys.readouterr()
    assert b is None
    assert "No scores available." in c.out


def test5(capsys) -> None:
    a = [11, 11, 11]
    b = summary_scores(a)
    c = capsys.readouterr()
    assert b is None
    assert ("You entered 3 scores\nAverage: 11.0\nHighest: 11\nLowest: 11\n") in c.out


def test6(capsys) -> None:
    a: list[int] = []
    b = clear_scores(a)
    c = capsys.readouterr()
    assert b is None
    assert "Scores cleared" in c.out


def test6(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "1")
    a = k()
    b = capsys.readouterr()
    assert a is None
    assert MENU in b.out


def test7(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "wuyihan")
    a = k()
    b = capsys.readouterr()
    assert a is None
    assert MENU in b.out
    assert "Invalid input.please input a number from 1 to 4." in b.out
