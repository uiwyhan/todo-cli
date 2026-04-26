from demo_project.storage import scores_load, scores_save


def test1(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("demo_project.storage.SCORE_FILE", tmp_path / "scores.json")
    a = [11, 12, 13, 14]
    scores_save(a)
    b = scores_load()
    assert b == a


def test2(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("demo_project.storage.SCORE_FILE", tmp_path / "score.json")
    b = scores_load()
    assert b == []
