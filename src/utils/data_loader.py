import pandas as pd
import os
from ..config import CSV_FILES

def load_dataset(dataset_name):
    """Load a specific dataset by name"""
    if dataset_name not in CSV_FILES:
        raise ValueError(f"Dataset {dataset_name} not found")
    
    file_path = CSV_FILES[dataset_name]
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    return pd.read_csv(file_path)

def load_all_datasets():
    """Load all datasets"""
    datasets = {}
    for name in CSV_FILES:
        try:
            datasets[name] = load_dataset(name)
        except Exception as e:
            print(f"Error loading {name}: {str(e)}")
    return datasets