import numpy as np

from src.utils.model_utils import predict


class DummyScaler:
    def transform(self, features):
        return features


class DummyModelHigh:
    def predict_proba(self, _features):
        return [[0.1, 0.9]]


class DummyModelLow:
    def predict_proba(self, _features):
        return [[0.9, 0.1]]


def test_predict_high_risk_label():
    prob, label = predict(DummyModelHigh(), DummyScaler(), np.array([[1.0, 2.0, 3.0, 4.0]]))
    assert prob == 0.9
    assert label == "High Risk"


def test_predict_low_risk_label():
    prob, label = predict(DummyModelLow(), DummyScaler(), np.array([[1.0, 2.0, 3.0, 4.0]]))
    assert prob == 0.1
    assert label == "Low Risk"
