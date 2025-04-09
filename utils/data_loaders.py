import pandas as pd
import os

try:
    base_dir = os.path.dirname(__file__)  # works in .py files
except NameError:
    base_dir = os.getcwd()  # fallback for Jupyter Notebooks

DATA_DIR = os.path.abspath(os.path.join(base_dir, '..', 'data'))

def load_all_reviews_from_sephora(folder='sephora_skincare_reviews'):
    folder_path = os.path.join(DATA_DIR, 'raw', folder)

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {folder_path}")

    all_dfs = []
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        df['source_file'] = file  # optional
        all_dfs.append(df)

    return pd.concat(all_dfs, ignore_index=True)

def load_sephora_product_info_data(filename='sephora_product_info.csv'):
    path = os.path.join(DATA_DIR, 'raw', filename)
    return pd.read_csv(path)

def load_amazon_data(filename='amazon_skincare.csv'):
    path = os.path.join(DATA_DIR, 'raw', filename)
    return pd.read_csv(path)

def load_inci_data(filename='inci_df.csv'):
    path = os.path.join(DATA_DIR, 'raw', filename)
    return pd.read_csv(path)