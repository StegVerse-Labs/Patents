from __future__ import annotations

from pathlib import Path

from tools.lint_patent_drawings import lint_directory, lint_source


def test_valid_mermaid_source(tmp_path: Path) -> None:
    source = tmp_path / "PAT-999-FIG-01-overview.mmd"
    source.write_text("flowchart LR\n    A[100 Intake] --> B[110 Decision]\n", encoding="utf-8")
    result = lint_source(source)
    assert result["decision"] == "DRAWING_SOURCE_VALID"
    assert result["reference_numerals"] == ["100", "110"]


def test_unbalanced_source_is_invalid(tmp_path: Path) -> None:
    source = tmp_path / "PAT-999-FIG-02-bad.mmd"
    source.write_text("flowchart LR\n    A[100 Intake --> B[110 Decision]\n", encoding="utf-8")
    result = lint_source(source)
    assert result["decision"] == "INVALID_DRAWING_SOURCE"
    assert any("unbalanced" in item for item in result["errors"])


def test_directory_requires_at_least_one_source(tmp_path: Path) -> None:
    result = lint_directory(tmp_path)
    assert result["decision"] == "DRAWING_SOURCES_INVALID"
    assert result["source_count"] == 0
