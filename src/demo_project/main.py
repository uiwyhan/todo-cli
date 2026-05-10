import argparse
from pathlib import Path

from demo_project.models import s
from demo_project.service import TaskNotFoundError, f, g, h
from demo_project.storage import load_storage, save_storage


def main1(x: list) -> None:
    if not x:
        print("there is no task")
        return
    else:
        for i in x:
            print(i)
        return


def build_parser():
    a = argparse.ArgumentParser(description="ArgumentParser")
    b = a.add_subparsers(dest="command", required=True, help="add subparsers")
    c = b.add_parser("add", help="add")
    c.add_argument("title", help="title")
    b.add_parser("list", help="list")
    d = b.add_parser("done", help="done")
    d.add_argument("id", type=int, help="task id")
    e = b.add_parser("delete", help="delete task")
    e.add_argument("id", type=int, help="task id")
    iiii = a.parse_args()
    return iiii


def handle_add(x: Path, y: list[s], z) -> None:
    if z.title is None:
        print("please enter a title")
        return
    else:
        a = f(y, z.title)
        save_storage(x, y)
        print("you add a task ", a)
        return


def handle_done(x: Path, y: list[s], z) -> None:
    if z.id is None:
        print("please input a number")
        return
    else:
        a = g(y, z.id)
        save_storage(x, y)
        print("you alread have done the task ", a)
        return


def handle_delete(x: Path, y: list, z) -> None:
    if z.id is None:
        print("please input a id")
        return
    else:
        a = h(y, z.id)
        save_storage(x, y)
        print("you delete a task ", a)
        return


def main2():
    a: Path = Path("www.json")
    b: list[s] = load_storage(a)
    c = build_parser()
    if c.command is None:
        print("please input a command")
        return
    else:
        print("the command you enter is ", c.command)
        try:
            if c.command == "add":
                handle_add(a, b, c)
                return
            elif c.command == "list":
                main1(b)
                return
            elif c.command == "done":
                handle_done(a, b, c)
                return
            elif c.command == "delete":
                handle_delete(a, b, c)
                return
            else:
                print("the command {c.command} is not found")
        except TaskNotFoundError as e:
            print(e)


if __name__ == "__main__":
    main2()
