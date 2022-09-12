from contextlib import suppress
from json import JSONDecodeError
import random
from re import A
import time
from dbs.mongodb import TextMongoDatabase
import requests


from log.logger import Logs
from utils.util import get_env


mongodb = TextMongoDatabase()


def get_documents(keyword: str, page: int = 10):
    for _ in range(10):
        url = f"http://127.0.0.1:8015/istock/search?query={keyword}&page={page}&language=en"
        headers = {"accept": "application/json"}
        try:
            with suppress(JSONDecodeError):
                response = requests.request("GET", url, headers=headers)
                return response.json()
        except requests.exceptions.ConnectionError:
            continue
    raise Exception("Could not connect to the server")


keywords = ["samsung", "h&m", "carrefour", "electroplanet", "iphone"]
for keyword in keywords:
    for page in range(1, 10):
        documents = get_documents(keyword, page).get("results")
        if len(documents) == 0:
            break
        mongodb.insert_many(documents)
        time.sleep(random.randint(1, 5))
        Logs().info(f"Inserted {len(documents)} documents for {keyword} in page {page}")
    Logs().info(f"Inserted all documents for {keyword}")
