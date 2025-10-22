import kagglehub
import pandas as pd
import sqlite3
from pathlib import Path
from pydantic import BaseModel, field_validator
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

# Download latest version
path = kagglehub.dataset_download("minahilfatima12328/lifestyle-and-sleep-patterns")
print("Path to dataset files:", path)
dataset_dir = Path(path)
csv_files = list(dataset_dir.glob("*.csv"))
if not csv_files:
    raise FileNotFoundError("No CSV File found in the Kaggle Dataset")
csv_path = csv_files[0]
print(f"Using Dataset: {csv_path.name}")

df = pd.read_csv(csv_path)
df.to_csv('lifestyle_and_sleep_patterns.csv', index=False)