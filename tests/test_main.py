from demo_project.cli import handle_add,handle_list,handle_delete,handle_change
from demo_project.models import s
def test_add() ->None:
    a = [
        s("wuyihan",88),
        s("wuyiqian",77),
    ]
    handle_add(a,"wuyilin",99)
    assert len(a) == 3
    assert a[2].a == "wuyilin"
    assert a[2].b == 99
    

def test_delete()->None:
    a = [
        s("wuyihan",88),
        s("wuyiqina",99),
    ]
    b = handle_delete(a,"wuyihan")
    assert b is not None
    assert len(a) == 1
    assert b.a == "wuyihan"
    assert b.b == 88
def test_change() ->None:
    a = [
        s("wuyihan",88),
        s("wuyiqian",99),
    ]
    b = handle_change(a,"wuyihan",90)
    assert b is not None
    assert b.a == a[0].a
    assert b.b == 90
    assert a[0].b == 90
def test_list(capsys) ->None:
    a = [
        s("wuyihan",99)
    ]
    handle_list(a)
    b = capsys.readouterr()
    assert str(a[0]) in b.out