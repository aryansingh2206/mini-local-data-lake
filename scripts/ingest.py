import shutil
import os

SOURCE_FILE = "sample_data/sales.csv"   # your source
RAW_DIR = "raw/sales.csv"

os.makedirs("raw", exist_ok=True)
shutil.copy(SOURCE_FILE, RAW_DIR)

print("Ingestion complete → raw zone")
