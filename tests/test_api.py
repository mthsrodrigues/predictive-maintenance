from fastapi.testclient import TestClient

from predictive_maintenance.api import app


client = TestClient(app)


class FakeModel:
    def predict(self, X):
        return [42.0]


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict(monkeypatch):
    payload = {
        "unit_id": 1,
        "cycle": 31,
        "setting_1": -0.0006,
        "setting_2": -0.0004,
        "sensor_2": 642.58,
        "sensor_3": 1581.22,
        "sensor_4": 1400.6,
        "sensor_6": 21.61,
        "sensor_7": 554.36,
        "sensor_8": 2388.04,
        "sensor_9": 9046.19,
        "sensor_11": 47.47,
        "sensor_12": 521.66,
        "sensor_13": 2388.02,
        "sensor_14": 8138.62,
        "sensor_15": 8.4195,
        "sensor_17": 392,
        "sensor_20": 39.06,
        "sensor_21": 23.419,
    }

    feature_columns = [
        column
        for column in payload
        if column != "unit_id"
    ]

    fake_artifact = {
        "model": FakeModel(),
        "feature_columns": feature_columns,
    }

    monkeypatch.setattr(
        "predictive_maintenance.api.get_artifact",
        lambda: fake_artifact,
    )

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["unit_id"] == 1
    assert body["cycle"] == 31
    assert body["predicted_rul"] == 42.0