import joblib
from pathlib import Path

from predictive_maintenance.data import load_cmapss_data
from predictive_maintenance.evaluate import regression_metrics
from predictive_maintenance.features import (
    add_rul_target,
    get_capped_rul,
    get_feature_columns,
)
from predictive_maintenance.train import (
    split_by_engine,
    train_random_forest,
)


DATA_DIR = Path("data/raw/CMAPSSData")


train_df, _, _ = load_cmapss_data(DATA_DIR)

train_df = add_rul_target(train_df)

feature_columns = get_feature_columns(train_df)

train_data, val_data = split_by_engine(train_df)

X_train = train_data[feature_columns]
X_val = val_data[feature_columns]

y_train = get_capped_rul(train_data)
y_val = get_capped_rul(val_data)

model = train_random_forest(
    X_train,
    y_train,
)

predictions = model.predict(X_val)

metrics = regression_metrics(
    y_val,
    predictions,
)

print(f"MAE: {metrics['mae']:.2f}")
print(f"RMSE: {metrics['rmse']:.2f}")


MODEL_PATH = Path("models/random_forest_rul.joblib")
artifact = {
    "model": model,
    "feature_columns": feature_columns,
}

joblib.dump(artifact, MODEL_PATH)

print(f"Model saved to: {MODEL_PATH}")