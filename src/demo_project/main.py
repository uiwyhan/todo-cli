import argparse
from pathlib import Path

from demo_project.models import s
from demo_project.service import f as service_f
from demo_project.service import g, h
from demo_project.storage import load_storage, save_storage


def main1(x: list[s]) -> None:
    if not x:
        print("there is no task")
    else:
        for i in x:
            print(i.a, i.b, i.c)


def main2() -> None:
    a: Path = Path("www.json")
    b: list[s] = load_storage(a)
    c = argparse.ArgumentParser()
    c.add_argument("command", nargs="?")
    c.add_argument("value", nargs="?")
    d = c.parse_args()
    if not d.command:
        print("please enter a command")
        return
    else:
        print("your command is ", d.command)
        if d.command == "add":
            if not d.value:
                print("please input a value")
                return
            else:
                e = str(d.value)
                i = service_f(b, e)
                print("you add a task: ", i)
                save_storage(a, b)
                return
        elif d.command == "list":
            main1(b)
            return
        elif d.command == "done":
            if not d.value:
                print("please input a value")
                return
            else:
                try:
                    e = int(d.value)
                except ValueError as error:
                    print(f"{e},{error},please input a number for value")
                    return
                m = g(b, e)
                print(f"the task {m} is alread done")
                save_storage(a, b)
                return
        elif d.command == "delete":
            if not d.value:
                print("please input a value")
                return
            else:
                try:
                    e = int(d.value)
                except ValueError:
                    print("please input a number")
                    return
                m = h(b, e)
                print(f"you delete the task {m}")
                save_storage(a, b)
                return
        print("please input a proper command")
        return


if __name__ == "__main__":
    main2()
