from demo_project.cli import k


def test1(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "q")
    c = k()
    d = capsys.readouterr()
    assert c is True
    assert "it's over" in d.out


def test2(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    c = k()
    d = capsys.readouterr()
    assert c is False
    assert "Invalid input. please enter a number." in d.out


def test3(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "197")
    c = k()
    d = capsys.readouterr()
    assert c is False
    assert "Invalid input. please enter a number from 0 to 100." in d.out


def test4(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "11")
    c = k()
    d = capsys.readouterr()
    assert c is False
    assert "score: 11, grade: E" in d.out
