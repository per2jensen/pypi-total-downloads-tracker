# 📦 PyPI Total Downloads Tracker

A self-hosted, GitHub Actions-powered tool that tracks daily **PyPI download stats** and displays a **live total** in your project's `README.md` using a **Shields.io badge**.

It works entirely offline — no external services — using real data from [pypistats.org](https://pypistats.org/).

I use this on my [dar-backup project](https://github.com/per2jensen/dar-backup), take a look for a live demo.

---

## ✨ Features

- 📊 Tracks total PyPI downloads using `pypistats recent`
- 📈 Logs daily history in `downloads.json`
- 🛡️ Renders a live Shields.io badge
- 🔁 Updates automatically with GitHub Actions
- ✅ Minimal setup — just one script and one workflow

---

## 🚀 Quick Start

### 1. Fork, Clone or download a zip file

Click on the **Fork** button to create your own tracker repo.

Or clone it directly:

```bash
git clone https://github.com/per2jensen/pypi-total-downloads-tracker
cd pypi-total-downloads-tracker
```

You can also just download a zip file (click the blue **Code** button) and play with the script locally.

### 2. Configure your PyPI package

Edit track_downloads.py and set your package name and seed total:

``` text
PACKAGE_NAME = "your-package-name"
SEED_TOTAL = 5200  # your known downloads so far
```

### 3. Add the marker to your README

Add this line where you want the live total to appear:

``` text
<!--TOTAL_DOWNLOADS-->
```

The README.md will be automatically updated and the change committed to the repo.

Please observe that the script currently expects the marker to start at a line.

Example of how it looks:
> <!--TOTAL_DOWNLOADS--> 📦 Total PyPI downloads: 5284

### or you could

### 4. Add the badge to your README

You can also add this Shields.io (this uses an external service) badge:

Substitute this in the badge "code" below:

- YOUR_USERNAME       # Github username
- your-package-name   # PyPI package name

```markdown
[![Total Downloads](https://img.shields.io/badge/dynamic/json?color=blue&label=Total%20Downloads&query=total&url=https%3A%2F%2Fraw.githubusercontent.com%2FYOUR_USERNAME%2Fpypi-total-downloads-tracker%2Fmain%2Fdownloads.json)](https://pypi.org/project/your-package-name/)
```

### 5. Push and activate GitHub Actions

After editing, push everything to GitHub. The included workflow will run daily and update:

> downloads.json
>
> README.md

You can also trigger the workflow manually via the Actions tab.
The schedule is commented out in the workflow - remove the `#` and enjoy daily automatic updates to the download totals number :-)

## 📁 Project Structure

```text
.
├── track_downloads.py         # The main Python script
├── downloads.json             # Daily tracked data
├── README.md                  # Your project + live total
└── .github/
    └── workflows/
        └── update_downloads.yml  # The GitHub Action
```

## 📖 License

MIT — use it, fork it, improve it.

## Test cases

Make sure `pytest` is available

```bash
cd <path/to//git/pypi-total-downloads-tracker>
PYTHONPATH=. pytest
```

## 🙌 Credits

Inspired by the limitations of PyPI’s API and the desire for accurate, offline-tracked download counts.

Built with ❤️ and pypistats.
