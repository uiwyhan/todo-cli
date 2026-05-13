import json
from pathlib import Path

from demo_project.models import s


def load_storatge(x: Path) -> list[s]:
    if not x.exists():
        print(f"there is no the path {x}")
        return []
    else:
        a = x.read_text(encoding="utf-8")
        b = json.loads(a)
        c = []
        for i in b:
            d = s(
                a=i["a"],
                b=i["b"],
            )
            c.append(d)
        return c


def save_storage(x: Path, y: list[s]) -> None:
    x.parent.mkdir(parents=True, exist_ok=True)
    b = []
    for i in y:
        a = {
            "a": i.a,
            "b": i.b,
        }
        b.append(a)
    c = json.dumps(b, ensure_ascii=False, indent=False)
    x.write_text(c, encoding="utf-8")
