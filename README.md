# 📦 PyPI Total Downloads Tracker

[![](https://img.shields.io/badge/readme-auto--update-blue)](https://github.com/per2jensen/pypi-total-downloads-tracker)

> 📦 Track total PyPI downloads for your package — with real stats and a live badge, powered by GitHub Actions.

A self-hosted, GitHub Actions-powered tool that tracks daily **PyPI download stats** and displays a **live total** in your project's `README.md` using a **Shields.io badge**.

It works entirely offline — no external services — using real data from [pypistats.org](https://pypistats.org/).

> **Live example**

I use it on my [dar-backup repo](https://github.com/per2jensen/dar-backup), take a look if interested.

---

## ✨ Features

- 📊 Fetches total PyPI downloads using `pypistats overall`
- 📝 Saves to a simple JSON file (`total` + `fetched`)
- 🛡️ Renders a live Shields.io badge
- 🔁 Updates automatically with GitHub Actions
- ✅ Minimal setup — just one script and one workflow

---

## 🚀 Quick Start

1. Clone this repo or use it as a **template** (see below).
2. Set your PyPI package name and seed total in `track_downloads.py`:

   ```python
   PACKAGE_NAME = "your-package-name"

   ```

3. Add these two markers to your `README.md` where you want the live number:

   ```markdown
   <!--PYPI_TOTAL_START-->
   📦 Total PyPI downloads: (this will be replaced)
   <!--PYPI_TOTAL_END-->
   ```

4. (Optional) Add a badge pointing to your `downloads.json`

   Replace "YOUR_USERNAME/YOUR_REPO" and "YOUR_PACKAGE" and drop the markdown shown below where you want the badge.

   ```markdown
   [![Total Downloads](https://img.shields.io/badge/dynamic/json?color=blue&label=Total%20Downloads&query=total&url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/downloads.json)](https://pypi.org/project/YOUR_PACKAGE/)
   ```

5. Push to GitHub — GitHub Actions will track downloads daily and update your badge/README!

---

## 🧪 Use as a Template

This repository is a GitHub **template** — click the blue  **“Use this template”** button at the top right of the page to create your own copy.

### 🧰 After creating your copy

1. Edit `track_downloads.py` to set your package name.
2. Add this block in your README:

   ```markdown
    <!--PYPI_TOTAL_START-->
    📦 Total PyPI downloads: [anything between the markers is replaced]
    <!--PYPI_TOTAL_END-->
   ```

3. Add the dynamic badge (see above) to display the live total.
4. Enable GitHub Actions in your new repo.
5. That's it! 🎉 Your downloads will be tracked and updated automatically.

---

## 📁 Project Structure

``` text
.
├── track_downloads.py         # The main Python script
├── downloads.json             # Total downloads & fetch date
├── README.md                  # Your project + live total
└── .github/
    └── workflows/
        └── update_downloads.yml  # The GitHub Action
```

---

## 📖 License

MIT — use it, fork it, improve it.

## Test cases

Make sure pytest is available

``` bash
cd <path/to//git/pypi-total-downloads-tracker>
PYTHONPATH=. pytest
```

---

## 🙌 Credits

Inspired by the limitations of PyPI’s API and the desire for accurate, offline-tracked download counts.

Built with ❤️ and `pypistats`.

---

## 🙋‍♀️ Used By

If you're using this template, [let me know](https://github.com/per2jensen/pypi-total-downloads-tracker/issues/new?assignees=&labels=template-usage&template=template-used.yml&title=%F0%9F%93%A6+I'm+using+this+template%21)

I'd love to showcase your project here.

### ⭐ Projects Using This Template

| Project | Description |
|---------|-------------|
| *(Your repo here?)* | Submit a quick issue and I'll add you! |
