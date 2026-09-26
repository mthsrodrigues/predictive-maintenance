import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def split_by_engine(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
):
    engine_ids = df["unit_id"].unique()

    train_engine_ids, val_engine_ids = train_test_split(
        engine_ids,
        test_size=test_size,
        random_state=random_state,
    )

    train_df = df[
        df["unit_id"].isin(train_engine_ids)
    ].copy()

    val_df = df[
        df["unit_id"].isin(val_engine_ids)
    ].copy()

    return train_df, val_df


def train_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> RandomForestRegressor:
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    return model