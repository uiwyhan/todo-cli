from demo_project.models import s


def test_model() -> None:
    a = s(a="wuyihan", b=88)
    assert a.a == "wuyihan"
    assert a.b == 88
