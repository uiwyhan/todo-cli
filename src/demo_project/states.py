import json
from pathlib import Path

a = [11, 12, 13, 14]
b = Path("www.json")
b.write_text(json.dumps(a, ensure_ascii=False), encoding="utf-8")
