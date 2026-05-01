import sys
from pathlib import Path

from demo_project.models import s
from demo_project.service import f, g, h
from demo_project.storage import load_storage, save_storage

a = Path("wuyihan.json")


def main1(x: list) -> list[s]:
    if not x:
        print("there is no task")
        return
    for i in x:
        b = "had done" if i.c else "not had done"
        print(f"{i.a},[{b}],{i.b}")


def main2():
    b = load_storage(a)
    if len(sys.argv) < 2:
        print("please enter a requirement:", "add/list/done/delet")
        return
    c = sys.argv[1]
    if c == "add":
        if len(sys.argv) < 3:
            print("please enter a title")
            return
        d = sys.argv[2]
        e = f(b, d)
        save_storage(a, b)
        print(f"{e.b} has added")
    elif c == "list":
        print(main1(b))
    elif c == "done":
        if len(sys.argv) < 3:
            print("please enter a number")
            return
        d = int(sys.argv[2])
        e = g(b, d)
        save_storage(a, b)
        print(f"{e.b} has added")
    elif c == "delete":
        if len(sys.argv) < 3:
            print("please enter a number")
            return
        d = int(sys.argv[2])
        e = h(b, d)
        save_storage(a, b)
        print(f"{e.b} has delete")
    else:
        print("please enter correct commant")


if __name__ == "__main__":
    main2()
