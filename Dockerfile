FROM python:3.8-slim-buster
LABEL authors="Armin"

COPY ./app /app
WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./models/PLUTO_Pipeline.pkl  /tmp/PLUTO_Pipelinev1.pkl
ENV MODEL_PATH=/tmp/PLUTO_Pipelinev1.pkl

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]