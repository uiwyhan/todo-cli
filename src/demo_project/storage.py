import json
from pathlib import Path

SCORE_FILE = Path("scores.json")


def scores_load() -> list[int]:
    if not SCORE_FILE.exists():
        return []
    with SCORE_FILE.open("r", encoding="utf-8") as g:
        a = json.load(g)
    return a


def scores_save(a: list[int]) -> None:
    with SCORE_FILE.open("w", encoding="utf-8") as f:
        json.dump(a, f)
