# User Stories

## Overview

This document contains user stories for the Data Science Final Project. User stories help define the features and functionality from an end-user perspective.

## Story Format

As a [user type], I want [goal] so that [benefit].

## User Stories

### Research and Analysis

#### US-1: Research Topics

- **As a** team member,
- **I want** to research the given topics from Telegram,
- **So that** I can understand the project requirements and context.
- **Task:** DSFP-1
- **Assignee:** MA
- **Status:** IN PROGRESS
- **Acceptance Criteria:**
  - Produce a short research summary (1-2 pages) listing relevant features, dataset limitations, and suggested analyses
  - Identify at least 3 key analysis questions (e.g., temporal trends, station demand, rider demographics)
  - Capture links to any external resources and the Telegram thread used for requirements

#### US-2: Dataset Analysis

- **As a** data analyst,
- **I want** to analyze the Ford GoBike dataset following the provided notebooks,
- **So that** I can understand the data structure, quality, and key insights.
- **Task:** DSFP-3
- **Assignee:** MA
- **Status:** TO DO
- **Acceptance Criteria:**
  - Complete exploratory data analysis (EDA) covering summary statistics, missingness, and distributions
  - Identify and document data quality issues and recommended fixes (e.g., outliers, missing timestamps)
  - Provide analyses for: trip duration distributions, hourly/daily patterns, station usage heatmaps, user type breakdowns, and correlation analysis
  - Produce reproducible notebooks and export key figures to `docs/` or `reports/`

### Documentation

#### US-3: Project Documentation

- **As a** team member or stakeholder,
- **I want** comprehensive project documentation,
- **So that** I can understand the project structure, progress, and decisions.
- **Task:** DSFP-2
- **Assignee:** AS
- **Status:** TO DO
- **Acceptance Criteria:**
  - Complete project plan and README with run/deploy steps
  - Sprint planning documentation and retrospective notes
  - User stories and team roles documented in `docs/`
  - Provide a short contributor guide (how to run notebooks, regenerate processed data)

### Development

#### US-4: Interactive Dashboard

- **As a** user,
- **I want** a clean and interactive dashboard,
- **So that** I can explore the Ford GoBike data visually and gain insights.
- **Task:** DSFP-4
- **Assignee:** AE
- **Status:** TO DO
- **Acceptance Criteria:**
  - Dashboard implemented in Streamlit (or Dash) with modular pages/sections
  - Core features: date range filter, station filter, user type filter, and download CSV option
  - Required visualizations: map of station usage, time-series of trips, trip duration histogram, weekday/hour heatmap, and top N stations by trips
  - Interactions: hover tooltips, selection-based filtering, and ability to export current view data
  - Responsive layout for common desktop and tablet resolutions

#### US-5: Analysis Pipelines

- **As a** data scientist,
- **I want** automated analysis pipelines,
- **So that** I can process data efficiently and reproducibly.
- **Task:** DSFP-5
- **Assignee:** MM
- **Status:** TO DO
- **Acceptance Criteria:**
  - Provide scripts (e.g., `src/` or `utils/processing_utils.py`) to ingest raw CSV and output cleaned CSV/Parquet in `data/processed/`
  - Pipelines include data validation, cleaning, basic feature engineering (time features, duration buckets), and logging
  - Pipeline outputs: `fordgobike_processed.csv`, summary statistics JSON, and precomputed aggregates for dashboard
  - Steps are reproducible and documented with example commands

### Deployment

#### US-6: Deployed Application

- **As a** end user,
- **I want** access to a deployed application,
- **So that** I can use the dashboard without local setup.
- **Task:** DSFP-6
- **Assignee:** MA
- **Status:** TO DO
- **Acceptance Criteria:**
  - Application deployed to Streamlit Community Cloud or Render and accessible via public URL
  - Performance: primary dashboard views load within ~3 seconds for typical queries on demo dataset
  - Availability: demo site reachable during working hours; aim for 99% availability for the demo period
  - Security: no sensitive credentials in repo; secrets handled via platform environment variables

### Optional Features

#### US-7: Predictive ML Models

- **As a** user,
- **I want** predictive machine learning models,
- **So that** I can make predictions about station demand or trip duration.
- **Task:** DSFP-7
- **Assignee:** [Unassigned]
- **Status:** TO DO (Optional)
- **Priority:** Low
- **Acceptance Criteria:**
  - Define prediction use case (e.g., short-term demand forecasting per station or trip duration prediction)
  - Provide baseline model and evaluation (train/validation split, metrics such as RMSE or MAE for continuous targets)
  - Model packaged with inference script and documented integration points for the dashboard

## Story Priority

1. High Priority:
   - US-1: Research Topics
   - US-2: Dataset Analysis
   - US-3: Project Documentation
   - US-4: Interactive Dashboard
   - US-5: Analysis Pipelines
   - US-6: Deployed Application

2. Optional:
   - US-7: Predictive ML Models

## Dependencies

- US-2 depends on US-1 (Research completion)
- US-4 depends on US-2 (Dataset analysis)
- US-5 depends on US-2 (Dataset analysis)
- US-6 depends on US-4 and US-5 (Dashboard and pipelines)
- US-7 depends on US-2 (Dataset analysis)
