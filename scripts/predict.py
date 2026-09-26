from pathlib import Path

import joblib

from predictive_maintenance.data import load_cmapss_data
from predictive_maintenance.evaluate import get_last_observations


DATA_DIR = Path("data/raw/CMAPSSData")
MODEL_PATH = Path("models/random_forest_rul.joblib")


_, test_df, test_rul = load_cmapss_data(DATA_DIR)

artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
feature_columns = artifact["feature_columns"]

test_last_rows = get_last_observations(test_df)

X_test = test_last_rows[feature_columns]

predictions = model.predict(X_test)

print("First predictions:")
print(predictions[:10])

print("\nTrue RUL:")
print(test_rul["rul"].head(10).to_numpy())