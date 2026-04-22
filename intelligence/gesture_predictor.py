from typing import List, Tuple, Dict
import numpy as np


class GesturePredictor:
    def __init__(self, model_manager, feature_extractor):
        self.model_manager = model_manager
        self.feature_extractor = feature_extractor

    def predict(self, points):
        if len(points) < 5:
            return {
                "gesture": None,
                "confidence": 0.0,
                "next_path": []
            }

        features = self.feature_extractor.extract_features(points)

        if features is None:
            return {
                "gesture": None,
                "confidence": 0.0,
                "next_path": []
            }

        gesture, confidence = self.model_manager.predict(features)

        return {
            "gesture": gesture,
            "confidence": confidence,
            "next_path": self._predict_next_path(points, gesture)
        }

    def _predict_next_path(self, points, gesture):
        if not gesture or len(points) < 2:
            return []

        last = points[-1]
        prev = points[-2]

        dx = last[0] - prev[0]
        dy = last[1] - prev[1]

        path = []
        x, y = last

        for i in range(1, 8):
            x += dx * 1.2
            y += dy * 1.2
            path.append((int(x), int(y)))

        return path