from pathlib import Path
import pandas as pd


def get_data():
    csv_path = Path(__file__).parent.parent / "data"

    data = {}

    for filepath in csv_path.iterdir():
        if filepath.suffix == ".csv":
            name = filepath.stem          # .csv uzantısını at
            name = name.replace("olist_", "")
            name = name.replace("_dataset", "")
            data[name] = pd.read_csv(filepath)

    return data
