import json
from pathlib import Path

from demo_project.models import s


def save_storage(x: Path, y: list[s]) -> None:
    x.parent.mkdir(parents=True, exist_ok=True)
    a = []
    for i in y:
        b = {
            "a": i.a,
            "b": i.b,
            "c": i.c,
        }
        a.append(b)
    c = json.dumps(a, ensure_ascii=False, indent=4)
    x.write_text(c, encoding="utf-8")


def load_storage(x: Path) -> list[s]:
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
