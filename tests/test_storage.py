from demo_project.models import s
from demo_project.storage import load_storage, save_storage


def test1(tmp_path):
    a = tmp_path / "aaa.json"
    b = []
    s1 = s(1, "wuyihan")
    b.append(s1)
    save_storage(a, b)
    c = load_storage(a)
    assert c == b
    assert c[0].a == 1
    assert c[0].b == "wuyihan"
    assert c[0].c is False


def test2(tmp_path):
    a = tmp_path / "aaa.json"
    b = load_storage(a)
    assert b == []


def test_save_tasks_creats_parent_directory(tmp_path) -> None:
    a = tmp_path / ".todo_cli" / "www.json"
    b = [s(1, "wuyihan")]
    save_storage(a, b)
    c = load_storage(a)
    assert a.exists()
    assert b == c
    assert b[0].a == 1
    assert b[0].b == "wuyihan"
    assert len(b) == 1
    assert b[0].c is False
