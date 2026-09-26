import pandas as pd

from predictive_maintenance.evaluate import get_last_observations


def test_get_last_observations():
    df = pd.DataFrame(
        {
            "unit_id": [1, 1, 2, 2],
            "cycle": [1, 2, 1, 3],
        }
    )

    result = get_last_observations(df)

    assert result["unit_id"].tolist() == [1, 2]
    assert result["cycle"].tolist() == [2, 3]