import requests
import os
import string
import random
from .utils import paths
from dotenv import load_dotenv

load_dotenv()
SERVER_URL = os.getenv("PRIVATE_SERVER_URL")


def __generate_session_id():
    characters = string.ascii_letters + string.digits
    session_key = ''.join(random.choice(characters) for _ in range(8))
    print(session_key)
    return session_key


def upload_files():
    file_paths = (paths.input_video, paths.audio)
    session_id = __generate_session_id()
    url = f"{SERVER_URL}/upload/{session_id}"

    files = [('file', (open(file_path, 'rb')))
             for file_path in file_paths]
    print(files)
    response = requests.post(url, files=files)

    print(response.json())
    return session_id
