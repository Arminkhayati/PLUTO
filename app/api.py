from fastapi import APIRouter, Depends, status
from models import PredictionOutput
import pluto_model as pm
import security as security


api = APIRouter()

pluto_model = pm.PLUTOModel()

@api.post("/predict/")
def post_predict(
    output: PredictionOutput = Depends(pluto_model.predict),
    authenticated: bool = Depends(security.validate_request),
) -> PredictionOutput:
    assert authenticated == True
    return output

# @api.delete("/cache/", status_code=status.HTTP_204_NO_CONTENT)
# def delete_cache():
#     pm.memory.clear()

@api.on_event("startup")
async def startup():
    pluto_model.load_model()

@api.get("/")
async def read_main():
    return {"msg": "Hello Walker & Dunlop"}