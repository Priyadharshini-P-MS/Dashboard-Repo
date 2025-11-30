# Witness Archive Dataset

This repository contains the dataset used in the **Witness Archive: Public Testimonies and News Narratives of ICE Raids in Chicago** project.

The goal of the project is to build a searchable, ethically sourced, and emotion‑tagged collection of narrative fragments drawn from public news reports and testimonies about ICE raids and immigration enforcement in Chicago.

## Contents

- `data/witness_archive_dataset.csv` – cleaned dataset of narrative fragments with metadata.

## Suggested Columns

Your CSV is expected to include columns similar to:

- `id` – unique identifier for each narrative fragment
- `title` – article or story title
- `source` – outlet or organization (e.g., WBEZ, ProPublica Illinois, Block Club Chicago)
- `date_published` – publication date
- `url` – link to the original article
- `text_excerpt` – short excerpt or narrative fragment
- `direct_quote` – flag for whether the excerpt is a direct quote or reporter description
- `emotion_label` – dominant emotion associated with the fragment (e.g., fear, sadness, anger, joy, neutral)
- `theme_label` – high‑level theme (e.g., family separation, legal barriers, detention conditions, community organizing)
- any additional fields you created for cleaning, tagging, or analysis

> Note: Column names may differ slightly depending on how you built the dataset.  
> You can update this README after upload to match the final schema.

## Usage

This dataset is intended for:

- exploratory analysis of emotions and themes in narratives about immigration enforcement,
- building dashboards (e.g., Streamlit) that allow filtering by source, date, emotion, and theme,
- supporting community‑driven research and teaching about the social and emotional impact of ICE raids.

Please ensure that any use of the data respects the ethical guidelines of your course, ChiEAC, and the original source outlets.

## Citation

If you share this dataset or a derivative, you may cite it as:

> Witness Archive: Public Testimonies and News Narratives of ICE Raids in Chicago (unpublished student project dataset).

You can adjust this citation to match any future publication details.