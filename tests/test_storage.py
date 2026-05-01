from demo_project.models import s
from demo_project.storage import load_storage, save_storage


def test1(tmp_path) -> None:
    a = tmp_path / "wuyihan.json"
    assert load_storage(a) == []


def test2(tmp_path) -> None:
    a = tmp_path / "wuyiqian.json"
    b = [s(1, "wuyihan"), s(2, "wuyiqian"), s(3, "heyuhua")]
    save_storage(a, b)
    c = load_storage(a)
    assert c == b
