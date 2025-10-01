from __future__ import annotations
import pandas as pd

def read_any(path_or_url: str) -> pd.DataFrame:
    """Read CSV or Parquet from local/remote (https/s3) using pandas + fsspec."""
    if path_or_url.lower().endswith('.parquet'):
        return pd.read_parquet(path_or_url)
    return pd.read_csv(path_or_url, parse_dates=['date'])
