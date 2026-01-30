<h1 align="center">🚴‍♂️ Ford GoBike Trip Analysis — Project Documentation</h1>

<p align="center">
	<img alt="badge" src="https://img.shields.io/badge/Status-Prototype-007ACC" />
	<img alt="badge" src="https://img.shields.io/badge/Tech-Python%20%7C%20Dash-2b9db9" />
	<img alt="badge" src="https://img.shields.io/badge/Docs-Complete-brightgreen" />
</p>

<p align="center">
	<img src="assets/images/1.png" alt="Dashboard overview" style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.12)" />
</p>

**Overview**

This repository contains a complete data science project that analyzes Ford GoBike trip data and provides an interactive Plotly Dash dashboard for exploration and insights. The project includes data processing pipelines, EDA notebooks, and reusable `src/` utilities.

**Quick Links & Structure**

- `dash_app.py` — Main Dash application entrypoint.
- `requirements.txt` — Python dependencies.
- `data/` — Raw and processed datasets (`raw/fordgobike_raw.csv`, `processed/fordgobike_processed.csv`).
- `notebooks/` — EDA and experiment notebooks.
- `src/`, `utils/` — Modules: `eda.py`, `plotting.py`, `processing_utils.py`.
- `assets/images/` — Screenshots used in this README and demos.
- `docs/` — Project plan, user stories, and sprint notes.

**Key Features**

- ✅ Interactive dashboard with filters (date range, station, user type)
- ✅ Preprocessing pipeline to produce `data/processed/fordgobike_processed.csv`
- ✅ EDA notebooks and exportable figures for reporting
- ✅ Map visualizations and time-series analytics

---

## Screenshots — Dashboard

<p align="center">
	<img src="assets/images/1.png" alt="Dashboard 1" width="48%" style="margin:4px;border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08)" />
	<img src="assets/images/2.png" alt="Dashboard 2" width="48%" style="margin:4px;border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08)" />
</p>

<p align="center">
	<img src="assets/images/3.png" alt="Dashboard 3" width="48%" style="margin:4px;border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08)" />
	<img src="assets/images/4.png" alt="Dashboard 4" width="48%" style="margin:4px;border-radius:6px;box-shadow:0 4px 10px rgba(0,0,0,0.08)" />
</p>

**Project Board (Jira)**

<p align="center">
	<img src="assets/images/image.png" alt="Jira board" width="70%" style="border-radius:6px;" />
</p>

---

## Getting started (local)

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Start the Dash app:

```powershell
python dash_app.py
```

3. Open the browser at the address printed by the app (usually `http://127.0.0.1:8050`).

---

## Data & Notebooks

- Raw: `data/raw/fordgobike_raw.csv`
- Processed: `data/processed/fordgobike_processed.csv` (produced by `utils/processing_utils.py`)
- Notebooks: `notebooks/` — EDA, preprocessing, model experiments

## Development notes

- Reuse functions in `src/` and `utils/` for plotting and pipeline steps.
- See `docs/project_plan.md` and `docs/user_stories.md` for scope and priorities.

---

**Contributors:** see `docs/team_roles.md`

Last updated: 2026-01-30
