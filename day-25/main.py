

#data = pd.read_csv("day-25\weather.csv")
#print(data)
# ...existing code...
import pandas as pd
import os
from pathlib import Path
import sys

print("cwd:", Path.cwd())
print("script:", Path(__file__).resolve())

base = Path(__file__).resolve().parent
csv_path = base / "weather.csv"
print("expected csv path:", csv_path)

if not csv_path.exists():
    print("ERROR: weather.csv not found at expected location.")
    print("Files in folder:", [p.name for p in base.iterdir()])
    sys.exit(1)

data = pd.read_csv(csv_path)
print(data.head())
# ...existing code...