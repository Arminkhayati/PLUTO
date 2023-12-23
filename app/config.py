import os

# MODEL_PATH = os.path.join("../models", "PLUTO_Pipeline.pkl")
MODEL_PATH = os.getenv("MODEL_PATH", "/tmp/PLUTO_Pipelinev1.pkl")
TOKEN = os.getenv("TOKEN", "2023")