import argparse
from pathlib import Path

from demo_project.models import s
from demo_project.service import f, g, h
from demo_project.storage import load_storage, save_storage


def main1(x: list[s]) -> None:
    for i in x:
        print(i.a, i.b, i.c)
    return


def main2():
    a: Path = Path("www.json")
    b: list[s] = load_storage(a)
    aa = argparse.ArgumentParser(description="subparser")
    bb = aa.add_subparsers(dest="command", required=True)
    aaa = bb.add_parser("add", help="add tasks")
    aaa.add_argument("title", type=str, help="task title")
    bb.add_parser("list", help="check up tasks")
    aaaa = bb.add_parser("done", help="done the task")
    aaaa.add_argument("id", type=int, help="task id")
    a2 = bb.add_parser("delete", help="delete the task")
    a2.add_argument("id", type=int, help="task id")
    c = aa.parse_args()
    if not c.command:
        print("please input a command")
    else:
        print("the command you enter is ", c.command)
        if c.command == "add":
            if not c.title:
                print("please input a title")
                return
            else:
                d = f(b, c.title)
                save_storage(a, b)
                print("you add a new task: ", d)
                return
        elif c.command == "list":
            main1(b)
            return
        elif c.command == "done":
            if c.id is None:
                print("please input a id")
                return
            else:
                try:
                    d = g(b, c.id)
                except ValueError:
                    print("e", c.id)
                    return
                save_storage(a, b)
                print("you finish a task: ", d)
        elif c.command == "delete":
            if c.id is None:
                print("please enter a id")
                return
            else:
                d = h(b, c.id)
                save_storage(a, b)
                print("you have deleted a task ", d)
                return
        else:
            print("please enter a proper command")
            return


if __name__ == "__main__":
    main2()
