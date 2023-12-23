from pluto_pipeline import PLOTUPipeline
from typing import List, Optional, Tuple
from config import MODEL_PATH
import pickle
import pandas as pd
from models import PredictionInput, PredictionOutput
import joblib

class PLUTOModel:
    model: Optional[PLOTUPipeline]

    def load_model(self):
        """Loads the model"""
        with open(MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        """Runs a prediction"""
        if not self.model:
            raise RuntimeError("Model is not loaded")
        model_inp = pd.DataFrame({k: [v] for k, v in input.__dict__.items()})
        prediction = self.model.pipe.predict(model_inp)
        category = bool(prediction[0])
        return PredictionOutput(category=category)