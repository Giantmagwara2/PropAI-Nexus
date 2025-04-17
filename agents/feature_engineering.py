# src/feature_engineering.py

import pandas as pd
import os

PROCESSED_DATA_DIR = 'data/processed'

def load_data(file_name):
    path = os.path.join(PROCESSED_DATA_DIR, file_name)
    return pd.read_csv(path)

def create_features(df):
    # Example: Price per square meter
    df['price_per_sqm'] = df['price'] / df['area']

    # Example: Year built features
    if 'year_built' in df.columns:
        df['property_age'] = pd.Timestamp.now().year - df['year_built']

    return df

def run_feature_engineering():
    df = load_data('property_data_clean.csv')
    df_features = create_features(df)

    df_features.to_csv(os.path.join(PROCESSED_DATA_DIR, 'property_data_features.csv'), index=False)
    print("✅ Feature engineering complete.")

if __name__ == '__main__':
    run_feature_engineering()
