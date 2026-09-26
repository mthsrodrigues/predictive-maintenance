import pandas as pd


CONSTANT_COLUMNS = [
    "setting_3",
    "sensor_1",
    "sensor_5",
    "sensor_10",
    "sensor_16",
    "sensor_18",
    "sensor_19",
]


def add_rul_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    max_cycles = df.groupby("unit_id")["cycle"].transform("max")
    df["rul"] = max_cycles - df["cycle"]

    return df


def get_feature_columns(df: pd.DataFrame) -> list[str]:
    return [
        column
        for column in df.columns
        if column not in CONSTANT_COLUMNS + ["unit_id", "rul"]
    ]


def get_capped_rul(df: pd.DataFrame, cap: int = 125) -> pd.Series:
    return df["rul"].clip(upper=cap)