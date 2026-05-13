from argparse import ArgumentParser, Namespace
from pathlib import Path

from demo_project.models import s
from demo_project.service import average_score, top_student
from demo_project.storage import load_storatge, save_storage

path = Path("aaaa.json")


def build_parser() -> ArgumentParser:
    a = ArgumentParser()
    b = a.add_subparsers(dest="command", required=True, help="subparser")
    c = b.add_parser("add", help="add")
    c.add_argument("name", help="name")
    c.add_argument("score", type=int, help="score")
    b.add_parser("list", help="list")
    d = b.add_parser("delete", help="delete")
    d.add_argument("name", help="name")
    e = b.add_parser("change", help="change")
    e.add_argument("name", help="name")
    e.add_argument("score", type=int, help="score")
    b.add_parser("average", help="average")
    b.add_parser("top_student", help="top student")
    return a


def handle_list(x: list[s]) -> None:
    a = average_score(x)
    b = top_student(x)
    for i in x:
        print(i)
    print(f"the average is: {a}")
    if b is None:
        print("there is no student")
    else:
        print(f"the average is {b.b}")


def handle_add(x: list[s], y: str, z: int) ->s:
    a = s(y, z)
    x.append(a)
    return a


def handle_delete(x: list[s], y: str) -> s|None:
    for i in x:
        if i.a == y:
            x.remove(i)
            return i
    return None


def handle_change(x: list[s], y: str, z: int) -> s|None:
    for i in x:
        if i.a == y:
            i.b = z
            return i
    return None


def main() -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    a = path
    b = load_storatge(a)
    c = build_parser().parse_args()
    print("the command is: {c.command}")
    if c.command == "add":
        if c.name is None:
            print("please input the name of the students")
            return
        elif c.score is None:
            print("please enter the score of the student")
            return
        else:
            d = handle_add(b, c.name, c.score)
            save_storage(a, b)
            print(f"{d} has been added")
            return
    elif c.command == "list":
        handle_list(b)
        return
    elif c.command == "delete":
        if c.name is None:
            print("please enter a name")
            return
        else:
            d1 = handle_delete(b, c.name)
            if d1 is None:
                print("there is no the student")
                return
            else:
                save_storage(a, b)
                print("{d1} has beed deleted")
                return
    elif c.command == "change":
        if c.name is None:
            print("please input a name")
            return
        else:
            d1 = handle_change(b, c.name, c.score)
            if d1 is None:
                print("there is no the student")
                return
            else:
                save_storage(a, b)
                print("{d1} has been deleted")
                return
