import json
from pathlib import Path

from demo_project.models import s


def save_storage(x: Path, y: list) -> None:
    a = []
    for i in y:
        b = {
            "a": i.a,
            "b": i.b,
            "c": i.c,
        }
        a.append(b)
    a = json.dumps(a, ensure_ascii=False, indent=3)
    x.write_text(a, encoding="utf-8")


def load_storage(x: Path) -> list:
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


a = load_storage(Path("aaa.json"))
for i in a:
    print(i.a, i.b, i.c)
