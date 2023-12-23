from pydantic import BaseModel

class PredictionOutput(BaseModel):
    category: bool