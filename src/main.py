import logging
from logging.config import dictConfig
from src.log_config import log_config # this is your local file

from pydantic import BaseModel

from transformers import pipeline

from fastapi import FastAPI

logging.config.dictConfig(log_config)

logger = logging.getLogger("reddit-broker-bot") # name of logger in loggers dict

app = FastAPI()

@app.get("/")
async def root():
    logger.info('/')
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    logger.info('/health')
    return {"message": "Healthy"}

class PredictionRequest(BaseModel):
    query_string: str


@app.on_event("startup")
def load_model():
    global sentiment_model
    sentiment_model = pipeline("sentiment-analysis")

@app.post("/my-endpoint")
def my_endpoint(request: PredictionRequest):
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    print(f"Sentiment test: {sentiment_query_sentence} = {sentiment}")
    return {"sentiment": sentiment}
