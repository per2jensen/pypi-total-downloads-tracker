
import json
import pytest
from datetime import datetime, UTC
from pathlib import Path

# We're testing the block-marker version
import track_downloads as tracker


def test_save_download_data_format(tmp_path, monkeypatch):
    # Redirect output file
    json_file = tmp_path / "downloads.json"
    monkeypatch.setattr(tracker, "JSON_FILE", json_file)

    # Run save function
    tracker.save_download_data(12345)

    data = json.loads(json_file.read_text())
    assert "total" in data
    assert "fetched" in data
    assert data["total"] == 12345

    today = datetime.now(UTC).strftime("%Y-%m-%d")
    assert data["fetched"] == today




def test_update_readme_block_markers(tmp_path):
    # Setup test README with START and END markers
    readme_path = tmp_path / "README.md"
    tracker.README_FILE = readme_path

    readme_content = (
        "# My Project\n"
        "Some intro text.\n"
        f"{tracker.START_MARKER}\n"
        "Old content\n"
        f"{tracker.END_MARKER}\n"
        "Footer text.\n"
    )
    readme_path.write_text(readme_content)

    tracker.update_readme(1234)
    updated = readme_path.read_text()

    assert f"{tracker.START_MARKER}\n📦 Total PyPI downloads: 1234\n{tracker.END_MARKER}" in updated


def test_multiple_runs_do_not_duplicate(tmp_path):
    readme_path = tmp_path / "README.md"
    tracker.README_FILE = readme_path

    readme_content = (
        "# Another Project\n"
        f"{tracker.START_MARKER}\n"
        "Initial content\n"
        f"{tracker.END_MARKER}\n"
    )
    readme_path.write_text(readme_content)

    tracker.update_readme(1111)
    tracker.update_readme(2222)
    tracker.update_readme(3333)

    updated = readme_path.read_text()

    # Should only have ONE 📦 line between the markers
    assert updated.count("📦 Total PyPI downloads:") == 1
    assert "📦 Total PyPI downloads: 3333" in updated


