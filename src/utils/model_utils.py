import pickle
from typing import Any, Tuple

import numpy as np


def load_artefacts(model_path: str, scaler_path: str) -> Tuple[Any, Any]:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler


def predict(model: Any, scaler: Any, features: np.ndarray) -> Tuple[float, str]:
    scaled = scaler.transform(features)
    probability = float(model.predict_proba(scaled)[0][1])
    label = "High Risk" if probability > 0.5 else "Low Risk"
    return probability, label
