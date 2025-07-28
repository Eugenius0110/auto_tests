import os
from dotenv import load_dotenv
import requests
import  pytest

load_dotenv() # подтянет файлик env, метод для подгрузки переменных окружения

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://relesase-gs.qa-playground.com/api/v1"

@pytest.fixture(autouse=True, scope="session")
def init_environment():
    responce = requests.post(
        url=f"{HOST}/setup",
        headers={
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
        }
    )
    assert responce.status_code == 205