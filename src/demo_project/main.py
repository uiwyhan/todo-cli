from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from demo_project.models import s
from demo_project.service import (
    StudentAlreadExistError,
    StudentNotFoundError,
    average_score,
    top_student,
)
from demo_project.storage import load_storatge, save_storage

path = Path("aaaa.json")
path.parent.mkdir(parents=True, exist_ok=True)


def score_type(x: str) -> int:
    try:
        a = int(x)
    except ValueError as error:
        raise ArgumentTypeError("please input a number") from error
    if a < 0 or a > 100:
        raise ArgumentTypeError("please input a number from 0 to 100")
    return  a


def build_parser() -> ArgumentParser:
    a = ArgumentParser()
    b = a.add_subparsers(dest="command", required=True, help="subparser")
    c = b.add_parser("add", help="add")
    c.add_argument("name", help="name")
    c.add_argument("score", type=score_type, help="score")
    b.add_parser("list", help="list")
    d = b.add_parser("delete", help="delete")
    d.add_argument("name", help="name")
    e = b.add_parser("change", help="change")
    e.add_argument("name", help="name")
    e.add_argument("score", type=score_type, help="score")
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


def find_student(x: list[s], y: str) -> s | None:
    for i in x:
        if i.a == y:
            print(f"the score of the student {y} is: {i.b}")
            return i
    return None


def handle_add(x: list[s], y: str, z: int) -> s:
    if find_student(x, y) is None:
        a = s(y, z)
        x.append(a)
        return a
    else:
        raise StudentAlreadExistError(f"the student {y} alread exist")


def handle_delete(x: list[s], y: str) -> s | None:
    if find_student(x, y) is not None:
        for i in x:
            if i.a == y:
                x.remove(i)
                return i
    else:
        raise StudentNotFoundError(f"the student {y} not found")
    return None


def handle_change(x: list[s], y: str, z: int) -> s | None:
    if find_student(x, y) is not None:
        for i in x:
            if i.a == y:
                i.b = z
                return i
    else:
        raise StudentNotFoundError(f"the student {y} is not found")
    return None


def main() -> int:
    a = path
    b = load_storatge(a)
    c = build_parser().parse_args()
    print(f"the command is: {c.command}")
    try:
        if c.command == "add":
            if c.name is None:
                print("please input the name of the students")
                return 1
            elif c.score is None:
                print("please enter the score of the student")
                return 1
            else:
                d = handle_add(b, c.name, c.score)
                save_storage(a, b)
                print(f"{d} has been added")
                return 0

        elif c.command == "list":
            handle_list(b)
            return 0
        elif c.command == "delete":
            if c.name is None:
                print("please enter a name")
                return 0
            else:
                d1 = handle_delete(b, c.name)
                if d1 is None:
                    print("there is no the student")
                    return 0
                else:
                    save_storage(a, b)
                    print("{d1} has beed deleted")
                    return 0
        elif c.command == "change":
            if c.name is None:
                print("please input a name")
                return 0
            else:
                d1 = handle_change(b, c.name, c.score)
                if d1 is None:
                    print("there is no the student")
                    return 0
                else:
                    save_storage(a, b)
                    print("{d1} has been deleted")
                    return 0
        else:
            return 1
    except ArgumentTypeError as error:
        print(error)
        return 1
    except StudentAlreadExistError as error:
        print(error)
        return 1
    except StudentNotFoundError as error:
        print(error)
        return 1
