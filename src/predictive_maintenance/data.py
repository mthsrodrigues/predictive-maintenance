from pathlib import Path

import pandas as pd


COLUMNS = (
    ["unit_id", "cycle"]
    + [f"setting_{i}" for i in range(1, 4)]
    + [f"sensor_{i}" for i in range(1, 22)]
)


def load_cmapss_data(data_dir: Path):
    train_df = pd.read_csv(
        data_dir / "train_FD001.txt",
        sep=r"\s+",
        header=None,
        names=COLUMNS,
    )

    test_df = pd.read_csv(
        data_dir / "test_FD001.txt",
        sep=r"\s+",
        header=None,
        names=COLUMNS,
    )

    test_rul = pd.read_csv(
        data_dir / "RUL_FD001.txt",
        sep=r"\s+",
        header=None,
        names=["rul"],
    )

    return train_df, test_df, test_rul