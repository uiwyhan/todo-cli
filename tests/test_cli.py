from demo_project.cli import k


def test1(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "q")
    a: list[int] = []
    b = k(a)
    c = capsys.readouterr()
    assert b is True
    assert "it's over" in c.out


def test2(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    a: list[int] = []
    b = k(a)
    c = capsys.readouterr()
    assert b is False
    assert "Invalid input. please enter a number.\n" in c.out
