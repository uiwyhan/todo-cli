from demo_project.storage import scores_load, scores_save


def test1(tmp_path, monkeypatch) -> None:
    a = tmp_path / "scores.json"
    monkeypatch.setattr("SCORE_FILE", a)
    b = [11, 12, 13, 14]
    scores_save(b)
    c = scores_load()
    assert c is b


def test2(tmp_path, monkeypatch) -> None:
    a = tmp_path / "score.json"
    monkeypatch.setattr("SECORE_FILE", a)
    b = [11, 12, 13]
    scores_save(b)
    c = scores_load()
    assert c is b
