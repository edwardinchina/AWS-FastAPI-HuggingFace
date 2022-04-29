import logging
from logging.config import dictConfig
from log_config import log_config # this is your local file

logging.config.dictConfig(log_config)

logger = logging.getLogger("reddit-broker-bot") # name of logger in loggers dict

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    logger.info('/')
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    logger.info('/health')
    return {"message": "Healthy"}

