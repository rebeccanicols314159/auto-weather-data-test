import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    API_KEY = "Token not available!"
    #logger.info("Token not available!")
    #raise

if __name__ == "__main__":
    logger.info(f"Token value: HIDDEN!")

    r = requests.get(f'https://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&q=CA13&num_of_days=1&format=json')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Temperature {r["current_condition"][0]["temp_C"]}°C')
    else:
        logger.info(f'Status code: {r.status_code}')
        logger.info(f'URL: {r}')
