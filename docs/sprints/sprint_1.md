# Sprint 1: DSFP Sprint 1

## Sprint Overview

- **Duration:** January 15 - January 29, 2025
- **Total Work Items:** 9
- **Sprint Goal:** Finish the project, bonus points if we can stay sane after.

## Sprint Tasks

#### DSFP-20: Setup GitHub Repo for Development

- **Assignee:** Mahmoud Taha
- **Description:** Set up the GitHub repository for collaborative development

#### DSFP-21: Initiate Project Files

- **Assignee:** Mahmoud Taha
- **Description:** Initialize project structure and necessary files

#### DSFP-1: Research Given Topics (Refer to Telegram)

- **Assignee:** Mahmoud Taha
- **Description:** Research topics as specified in Telegram

#### DSFP-2: Document the Entire Project

- **Assignee:** Aya Salah
- **Description:** Document the entire project, including sprint planning, stories, etc.
- **Acceptance Criteria:**
  - Complete project documentation in docs folder
  - Include sprint planning and user stories

#### DSFP-3: Analyze the Required Dataset

- **Status:** TO DO
- **Assignee:** Mahmoud Taha
- **Description:** Analyze the required dataset following the provided notebooks
- **Acceptance Criteria:**
- Reference notebooks: `notebooks/main.ipynb` and `notebooks/preprocessing.ipynb`
- Complete exploratory data analysis (summary stats, missingness, distributions)
- Document key findings, include visuals exported as PNGs into `docs/` or `reports/`
- Produce cleaned dataset in `data/processed/fordgobike_processed.csv`

#### DSFP-4: Develop a Clean and Interactive UI (Dashboard)

- **Assignee:** Aisha Essam
- **Description:** Create a clean and interactive dashboard for data visualization
- **Acceptance Criteria:**
  - Interactive visualizations
  - Responsive design
  - Prototype deployed locally or hosted, demonstrating at least two interactive visualizations (map + time series)

#### DSFP-5: Create Analysis Pipelines

- **Assignee:** Mohamed Monsef
- **Description:** Develop data analysis pipelines
- **Acceptance Criteria:**
  - Data processing pipelines
  - Analysis workflows
  - Provide runnable scripts (e.g., `scripts/` or `src/processing_utils.py`) to transform `data/raw/fordgobike_raw.csv` into `data/processed/` artifacts

#### DSFP-6: Deploy the Application

- **Assignee:** Mahmoud Taha
- **Description:** Deploy the application to production
- **Acceptance Criteria:**
  - Application accessible via URL
  - Add deployment notes, link to deployed demo where available (Streamlit Community Cloud or Render), or documented steps to deploy locally

#### DSFP-7: (Optional) Develop Predictive ML Models

- **Assignee:** [Unassigned]
- **Description:** Develop predictive machine learning models
- **Priority:** Optional

## Dependencies

- DSFP-3 depends on DSFP-1 (Research completion)
- DSFP-4 depends on DSFP-3 (Dataset analysis)
- DSFP-5 depends on DSFP-3 (Dataset analysis)
- DSFP-6 depends on DSFP-4 and DSFP-5 (UI and pipelines)
