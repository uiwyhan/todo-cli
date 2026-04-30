import json
from pathlib import Path
from demo_project.models import s


def save_storage(x: Path, y: list) -> None:
    b = []
    for i in y:
        a = {"a": i.a, "b": i.b, "c": i.c}
        b.append(a)
    c = json.dumps(b, ensure_ascii=False, indent=4)
    c.write_text(encoding="utf-8")


def load_storage(x: Path) -> list:
    if not x.exists():
        print("there is no this Path")
        return []
    a = []
    b = x.read_text(encoding="utf-8")
    c = json.loads(b)
    for i in c:
        d = s(
            i["a"],
            i["b"],
            i["c"],
        )
        a.append(d)
    return a
