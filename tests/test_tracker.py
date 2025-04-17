
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



def test_marker_replacement_preserves_line_content(tmp_path):
    # Test that the marker is replaced inline and surrounding text is preserved
    readme_path = tmp_path / "README.md"
    original_line = "📊 Stats: <!--TOTAL_DOWNLOADS--> updated daily.\n"
    readme_path.write_text(original_line)

    import track_downloads
    track_downloads.README_FILE = readme_path

    track_downloads.update_readme(4321, flagged=False)
    result = readme_path.read_text()
    expected = "📊 Stats: <!--TOTAL_DOWNLOADS--> 📦 Total PyPI downloads: 4321 updated daily.\n"
    assert result == expected

def test_warning_logged_on_repeated_count(capsys, tmp_path, monkeypatch):
    # Test that a warning is printed to the console when a count is repeated
    downloads_file = tmp_path / "downloads.json"
    monkeypatch.setattr("track_downloads.JSON_FILE", downloads_file)
    monkeypatch.setattr("track_downloads.SEED_TOTAL", 0)

    # Simulate history with one entry
    data = {
        "total": 36,
        "history": [{"date": "2025-04-16", "count": 36}]
    }
    downloads_file.write_text(json.dumps(data))

    # Patch date function to fix date
    import track_downloads
    yesterday = "2025-04-17"
    monkeypatch.setattr(track_downloads, "get_yesterday_date", lambda: yesterday)

    # Force same count (repeat)
    monkeypatch.setattr(track_downloads, "fetch_downloads_last_day", lambda _: 36)
    track_downloads.update_readme = lambda *args, **kwargs: None  # skip writing README

    track_downloads.main()
    captured = capsys.readouterr()
    assert "⚠️ Warning: Download count repeated (36) on 2025-04-17" in captured.out


def test_readme_displays_warning_on_repeated_count(tmp_path):
    readme_path = tmp_path / "README.md"
    original_line = "📊 Stats: <!--TOTAL_DOWNLOADS--> updated daily.\n"
    readme_path.write_text(original_line)

    import sys
    sys.modules.pop("track_downloads", None)  # Force reload with patched values

    import track_downloads
    track_downloads.README_FILE = readme_path
    track_downloads.MARKER = "<!--TOTAL_DOWNLOADS-->"  # just in case

    track_downloads.update_readme(1234, flagged=True)
    result = readme_path.read_text()

    print("=== README OUTPUT ===")
    print(result)

    expected = "📊 Stats: <!--TOTAL_DOWNLOADS--> 📦 Total PyPI downloads: 1234 ⚠️ Repeated count updated daily.\n"
    assert result == expected
