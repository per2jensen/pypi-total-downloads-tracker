# 📦 PyPI Total Downloads Tracker

A self-hosted, GitHub Actions-powered tool that tracks daily **PyPI download stats** and displays a **live total** in your project's `README.md` using a **Shields.io badge**.

It works entirely offline — no external services — using real data from [pypistats.org](https://pypistats.org/).

---

## ✨ Features

- 📊 Tracks total PyPI downloads using `pypistats recent`
- 📈 Logs daily history in `downloads.json`
- 🛡️ Renders a live Shields.io badge
- 🔁 Updates automatically with GitHub Actions
- ✅ Minimal setup — just one script and one workflow

---

## 🚀 Quick Start

### 1. Use this template

Click **“Use this template”** on GitHub to create your own tracker repo.

Or clone it directly:
```bash
git clone https://github.com/per2jensen/pypi-total-downloads-tracker
cd pypi-total-downloads-tracker
```

### 2. Configure your PyPI package

Edit track_downloads.py and set your package name and seed total:
```
PACKAGE_NAME = "your-package-name"
SEED_TOTAL = 5200  # your known downloads so far
```

### 3. Add the marker to your README

Add this line where you want the live total to appear:

```
<!--TOTAL_DOWNLOADS-->
```

It will be automatically updated to:

<!--TOTAL_DOWNLOADS--> 📦 Total PyPI downloads: 5284


or you could

### 4. Add the badge to your README

You can also add this Shields.io badge:

Substitute this in the badge "code" below:

-  YOUR_USERNAME       # Github username
-  your-package-name   # PyPI package name

```markdown
[![Total Downloads](https://img.shields.io/badge/dynamic/json?color=blue&label=Total%20Downloads&query=total&url=https%3A%2F%2Fraw.githubusercontent.com%2FYOUR_USERNAME%2Fpypi-total-downloads-tracker%2Fmain%2Fdownloads.json)](https://pypi.org/project/your-package-name/)
```

### 5. Push and activate GitHub Actions

After editing, push everything to GitHub. The included workflow will run daily and update:

    downloads.json

    README.md

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



## 🙌 Credits

Inspired by the limitations of PyPI’s API and the desire for accurate, offline-tracked download counts.

Built with ❤️ and pypistats.








