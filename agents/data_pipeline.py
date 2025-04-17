# src/data_pipeline.py

import pandas as pd
import numpy as np
import os

RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'

def load_raw_data(file_name):
    path = os.path.join(RAW_DATA_DIR, file_name)
    return pd.read_csv(path)

def clean_data(df):
    # Basic cleaning: nulls, duplicates, data types
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')

    # Example: Convert date columns
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    return df

def save_processed_data(df, file_name):
    path = os.path.join(PROCESSED_DATA_DIR, file_name)
    df.to_csv(path, index=False)

def run_pipeline():
    # Example with dummy file
    df_raw = load_raw_data('property_data.csv')
    df_clean = clean_data(df_raw)
    save_processed_data(df_clean, 'property_data_clean.csv')
    print("✅ Data pipeline complete.")

if __name__ == '__main__':
    run_pipeline()
