import sys
from pathlib import Path
from demo_project.service import f,g,h
from demo_project.models import s
from demo_project.storage import save_storage, load_storage
import json
a = Path("wuyihan.json")
def main1(x:list) ->list[s]:
    if not x:
        print("the list of tasks is nothing")
        return []
    for i in x:
        print(
           f"the coding is {i.a}, the title is {i.b}, the status of task is {i.c}"
        )
def main2()->None:
    b:list[s] = load_storage(a)
    c:list = sys.argv
    if len(c)<2:
        print("enter your command")
    else:
        d:str = c[1]
        if d == "add":
            print("you select the command 'add'")
            if len(c)<3:
                print("please enter your title")
            else:
                d:str = c[2]
                e = f(b,d)
                save_storage(a,b)
                print(f"you add the task ",e)
        elif d == "list":
            print("you enter the command 'list'")
            d = main1(b)
        elif d == "done":
            print("your command is ", d)
            if len(c)<3:
                print("please input your coding for your command 'done'")
            else:
                d = int(c[2])
                d = g(b,d)
                save_storage(a,b)
                print("you have done the task", d)
        elif d == "delete":
            print("you enter the command ", d)
            if len(c)<3:
                print("please enter the coding for the command 'delete'")
            else:
                d = int(c[2])
                d = h(b,d)
                save_storage(a,b)
                print(f"you have delete the task named {d}")
        else:
            print("please input correct command") 
if __name__ == "__main__":
    main2()