from pathlib import Path

from demo_project.models import s
from demo_project.storage import load_storatge, save_storage


def test_save_load_storage(tmp_path: Path) -> None:
    a = tmp_path / "parent" / "www.json"
    b = [
        s("wuyihan", 88),
        s("wuyiqian", 77),
    ]
    save_storage(a, b)
    c = load_storatge(a)
    assert b == c


def test_no_path_storage(tmp_path: Path) -> None:
    a = tmp_path / "parent" / "www.json"
    b = load_storatge(a)
    assert b == []
