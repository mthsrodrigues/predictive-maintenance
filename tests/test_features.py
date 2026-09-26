import pandas as pd

from predictive_maintenance.features import (
    add_rul_target,
    get_capped_rul,
)


def test_add_rul_target():
    df = pd.DataFrame(
        {
            "unit_id": [1, 1, 1],
            "cycle": [1, 2, 3],
        }
    )

    result = add_rul_target(df)

    assert result["rul"].tolist() == [2, 1, 0]


def test_get_capped_rul():
    df = pd.DataFrame(
        {
            "rul": [150, 125, 80, 0],
        }
    )

    result = get_capped_rul(df, cap=125)

    assert result.tolist() == [125, 125, 80, 0]