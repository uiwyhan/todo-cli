import argparse

a = argparse.ArgumentParser()
b = a.add_subparsers(dest="command", required=True)
c = b.add_parser("add", help="add a task")
c.add_argument("title", help="task title")
e = b.add_parser("list", help="show the task")
f = b.add_parser("done", help="finsh a task")
f.add_argument("id", type=int, help="task id")
h = b.add_parser("delete", help="delete task")
h.add_argument("id", type=int, help="task id")
args = a.parse_args
