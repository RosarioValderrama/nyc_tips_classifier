import pandas as pd

def load_dataset(parquet_url: str) -> pd.DataFrame:
    df = pd.read_parquet(parquet_url)
    return df

def add_target(df: pd.DataFrame, target_col: str = "high_tip") -> pd.DataFrame:
    df = df[df['fare_amount'] > 0].reset_index(drop=True)
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = (df['tip_fraction'] > 0.2).astype("int32")
    return df
