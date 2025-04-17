
import pytest
import json
from pathlib import Path
from track_downloads import get_yesterday_date, load_download_data, update_readme

def test_get_yesterday_date_format():
    date_str = get_yesterday_date()
    assert len(date_str) == 10  # YYYY-MM-DD
    assert date_str.count("-") == 2

def test_load_download_data_seed(tmp_path, monkeypatch):
    # Use temporary file location
    dummy_file = tmp_path / "downloads.json"
    monkeypatch.setattr("track_downloads.JSON_FILE", dummy_file)
    monkeypatch.setattr("track_downloads.SEED_TOTAL", 1234)

    data = load_download_data()
    assert data["total"] == 1234
    assert data["history"] == []

def test_update_readme(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text("Title\n<!--TOTAL_DOWNLOADS-->\nFooter\n")

    # Monkeypatch the path
    import track_downloads
    track_downloads.README_FILE = readme_path

    track_downloads.update_readme(9999)
    result = readme_path.read_text()
    assert "📦 Total PyPI downloads: 9999" in result

def test_update_readme_with_inline_marker(tmp_path):
    # Create a temporary README file with an inline marker
    readme_path = tmp_path / "README.md"
    readme_path.write_text("Some intro | Downloads: <!--TOTAL_DOWNLOADS--> as of now\n")

    # Patch the module's README_FILE path to use our temp file
    import track_downloads
    track_downloads.README_FILE = readme_path

    # Run the update function
    track_downloads.update_readme(8888)

    # Read and validate the result
    result = readme_path.read_text()
    assert "Downloads: <!--TOTAL_DOWNLOADS--> 📦 Total PyPI downloads: 8888 as of now" in result


