
import csv
import os
import sys


def main():
    # Compute path to weather.csv relative to this script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "weather.csv")

    # Diagnostics
    print(f"Script directory: {script_dir}")
    print(f"Looking for CSV at: {csv_path}")

    if not os.path.exists(csv_path):
        print("Error: CSV file not found at the computed path.")
        # Also show current working directory to help debug how script was launched
        print(f"Current working directory: {os.getcwd()}")
        print("Make sure 'weather.csv' is in the same folder as this script, or pass a correct path.")
        sys.exit(1)

    try:
        with open(csv_path, newline='') as data_file:
            data = csv.reader(data_file)
            rows = list(data)
            print(f"Read {len(rows)} rows from CSV")
            # Show first 5 rows as a sample
            for r in rows[:5]:
                print(r)
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()