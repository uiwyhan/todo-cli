from pathlib import Path

from demo_project.service import f, g
from demo_project.storage import save_storage


def main() -> None:
    a = []
    f(a, "wuyihan")
    f(a, "wuyiqian")
    f(a, "heyuhua")
    g(a, 1)
    g(a, 3)
    save_storage(Path("aaa.json"), a)


if __name__ == "__main__":
    main()
