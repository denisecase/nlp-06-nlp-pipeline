"""Offline smoke test for the web-document NLP pipeline stages."""

import logging
from types import SimpleNamespace

import matplotlib
import pandas as pd
import requests

from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform import run_transform
from nlp.stage04_analyze import run_analyze
from nlp.stage05_load import run_load

HTML = """<html><head><link rel="canonical" href="https://arxiv.org/abs/1234.56789"></head>
<body>
<h1 class="title">Title: NLP Example</h1>
<div class="authors"><a>Ada</a><a>Grace</a></div>
<blockquote class="abstract">
Abstract: Language models analyze text and compare model outputs.
</blockquote>
<div class="subheader">Subjects: Computation and Language</div>
<div class="dateline">Submitted on 1 January 2026</div>
</body></html>
"""


def test_nlp_stages_write_features_figures_and_csv(monkeypatch, tmp_path):
    """Run the real spaCy transform and analysis using a fixed HTML sample."""

    def fake_get(url, *, headers, timeout):
        assert url == "https://example.test/paper"
        assert "User-Agent" in headers
        assert timeout == 30
        return SimpleNamespace(text=HTML, raise_for_status=lambda: None)

    matplotlib.use("Agg")
    monkeypatch.setattr(requests, "get", fake_get)
    log = logging.getLogger(__name__)
    raw_path = tmp_path / "raw.html"
    csv_path = tmp_path / "processed.csv"
    output_dir = tmp_path / "processed"

    html = run_extract(
        "https://example.test/paper", {"User-Agent": "pytest"}, raw_path, log
    )
    df = run_transform(run_validate(html, log), log)
    run_analyze(df, LOG=log, output_dir=output_dir, top_n=5)
    run_load(df, csv_path, log)

    assert raw_path.read_text(encoding="utf-8") == HTML
    assert csv_path.stat().st_size > 0
    saved = pd.read_csv(csv_path)
    assert saved.loc[0, "title"] == "NLP Example"
    assert saved.loc[0, "author_count"] == 2
    assert saved.loc[0, "token_count"] > 0
    assert 0 < saved.loc[0, "type_token_ratio"] <= 1
    assert (output_dir / "case_top_tokens.png").stat().st_size > 0
    assert (output_dir / "case_wordcloud.png").stat().st_size > 0
