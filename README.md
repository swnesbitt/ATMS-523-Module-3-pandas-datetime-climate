# Grad Analytics: Pandas `groupby` + Datetime on Climate Data (with GHCN-from-Cloud)

This repository is a **self-contained in-class activity** showing idiomatic **pandas** `groupby` + **datetime** patterns
on climate data, now powered by a **cloud dataset** (NOAA GHCN Daily, public S3).

## What you'll do
1. (**Notebook 02**) Fetch Illinois GHCN daily data from NOAA's **public S3** for 4 stations with ≥30 years of record and write a **local Parquet** file.
2. (**Notebook 01**) Load that Parquet (or read via a **cloud HTTPS raw** URL once you push the repo) and perform `groupby`+datetime analytics:
   - Monthly means (per station), annual totals & rankings
   - Station-by-month climatology
   - Warm-season aggregations
   - Rolling/windowed stats per station
   - `groupby` vs `resample`

## Quick start

```bash
# conda/mamba
mamba env create -f environment.yml
mamba activate pandas-datetime-climate

# or pip
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Launch
jupyter lab
```

Open notebooks in this order:

- `notebooks/02_fetch_ghcn_il_to_parquet.ipynb` (creates `data/ghcn_il_top4_daily.parquet`)
- `notebooks/01_groupby_datetime.ipynb` (loads that Parquet and runs the analytics)

## Cloud-style access

After pushing this repo to GitHub, you can read the Parquet over **HTTPS** by setting:
```
CLOUD_PARQUET = "https://raw.githubusercontent.com/USER/REPO/main/data/ghcn_il_top4_daily.parquet"
```
in `01_groupby_datetime.ipynb`.

## Repo layout
```
grad-analytics-pandas-datetime-climate_v2/
├── data/
│   └── ghcn_il_top4_daily.parquet        # created by Notebook 02 (not committed by default)
├── notebooks/
│   ├── 01_groupby_datetime.ipynb          # the analysis exercise
│   └── 02_fetch_ghcn_il_to_parquet.ipynb  # cloud → parquet tutorial
├── src/
│   └── io_helpers.py
├── environment.yml
├── requirements.txt
└── README.md
```

## License
MIT
