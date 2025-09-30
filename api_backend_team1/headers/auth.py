
import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    auth_token = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }
