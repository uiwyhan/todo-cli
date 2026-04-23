from demo_project.cli import k


def test1(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "q")
    a = k()
    b = capsys.readouterr()
    assert a is True
    assert "it's over" in b.out


def test2(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "111")
    a = k()
    b = capsys.readouterr()
    assert a is False
    assert "Invalid input.please enter a number from 0 to 100."
