import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error


def regression_metrics(
    y_true,
    y_pred,
) -> dict:
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred) ** 0.5

    return {
        "mae": mae,
        "rmse": rmse,
    }


def get_last_observations(
    df: pd.DataFrame,
) -> pd.DataFrame:
    return (
        df.sort_values(["unit_id", "cycle"])
        .groupby("unit_id")
        .tail(1)
        .sort_values("unit_id")
    )