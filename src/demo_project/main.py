from demo_project.service import f, g, h


def k():
    a = []
    f(a, "wuyihan")
    f(a, "wuyiqian")
    f(a, "wuyilin")
    for i in a:
        print(i.a, i.b, i.c)
    g(a, 1)
    g(a, 3)
    for i in a:
        print(i.a, i.b, i.c)
    h(a, 2)
    for i in a:
        print(i.a, i.b, i.c)


if __name__ == "__main__":
    k()
