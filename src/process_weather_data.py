import os
import json
import pandas as pd

# Paths
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"

def process_latest_file():
    # Find the latest JSON file in data/raw
    files = [f for f in os.listdir(RAW_DATA_DIR) if f.endswith(".json")]
    if not files:
        print("⚠️ No raw data files found.")
        return
    
    latest_file = max(
        [os.path.join(RAW_DATA_DIR, f) for f in files],
        key=os.path.getctime
    )
    print(f"📂 Processing file: {latest_file}")

    # Load JSON
    with open(latest_file, "r") as f:
        data = json.load(f)
    
    # Extract hourly data
    hourly = data["hourly"]
    df = pd.DataFrame(hourly)

    # Convert to datetime
    df["time"] = pd.to_datetime(df["time"])

    # Save processed data
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    output_file = os.path.join(PROCESSED_DATA_DIR, "processed_weather.csv")
    df.to_csv(output_file, index=False)

    print(f"✅ Processed data saved to {output_file}")

if __name__ == "__main__":
    process_latest_file()

