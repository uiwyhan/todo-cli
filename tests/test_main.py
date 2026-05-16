from pathlib import Path

import pytest
from pytest import CaptureFixture, MonkeyPatch

import demo_project.main as tomain
from demo_project.main import (
    build_parser,
    handle_add,
    handle_change,
    handle_delete,
    handle_list,
)
from demo_project.models import s
from demo_project.service import StudentAlreadExistError, StudentNotFoundError


def test_add() -> None:
    a = [
        s("wuyihan", 88),
        s("wuyiqian", 77),
    ]
    handle_add(a, "wuyilin", 99)
    assert len(a) == 3
    assert a[2].a == "wuyilin"
    assert a[2].b == 99


def test_delete() -> None:
    a = [
        s("wuyihan", 88),
        s("wuyiqina", 99),
    ]
    b = handle_delete(a, "wuyihan")
    assert b is not None
    assert len(a) == 1
    assert b.a == "wuyihan"
    assert b.b == 88


def test_change() -> None:
    a = [
        s("wuyihan", 88),
        s("wuyiqian", 99),
    ]
    b = handle_change(a, "wuyihan", 90)
    assert b is not None
    assert b.a == a[0].a
    assert b.b == 90
    assert a[0].b == 90


def test_list(capsys: CaptureFixture[str]) -> None:
    a = [s("wuyihan", 99)]
    handle_list(a)
    b = capsys.readouterr()
    assert str(a[0]) in b.out


def test_type_error() -> None:
    a = build_parser()
    with pytest.raises(SystemExit):
        a.parse_args(["add", "wuyihan", "222"])
    with pytest.raises(SystemExit):
        a.parse_args(["add", "wuyiqina", "wwww"])


def test_add_error() -> None:
    a = [
        s("wuyihan", 88),
        s("wuyiqian", 99),
    ]
    with pytest.raises(StudentAlreadExistError):
        handle_add(a, "wuyihan", 11)


def test_delete_error() -> None:
    a = [
        s("wuyihan", 88),
        s("wuyiqian", 99),
    ]
    with pytest.raises(StudentNotFoundError):
        handle_delete(a, "wwww")


def test_add_command(
    tmp_path: Path, capsys: CaptureFixture[str], monkeypatch: MonkeyPatch
) -> None:
    a = tmp_path / "wuyihan" / "jjj.json"
    monkeypatch.setattr(tomain, "path", a)
    monkeypatch.setattr("sys.argv", ["todo", "add", "wuyihan", "88"])
    b = tomain.main()
    c = capsys.readouterr()
    assert "the command is: add" in c.out
    assert "s(a='wuyihan', b=88) has been added" in c.out
    assert b == 0


def test_list_command(
    tmp_path: Path, capsys: CaptureFixture[str], monkeypatch: MonkeyPatch
) -> None:
    a = tmp_path / "wuyihan" / "jjj.json"
    monkeypatch.setattr(tomain, "path", a)
    monkeypatch.setattr("sys.argv", ["todo", "list"])
    b = tomain.main()
    c = capsys.readouterr()
    assert f"there is no the path {a}" in c.out
    assert "there is no student" in c.out
    assert b == 0
