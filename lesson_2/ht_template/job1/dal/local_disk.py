import json
import os.path
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    file_path = get_file_path(path)
    with open(file_path, 'w') as file:
        json.dump(json_content, file)

def get_file_path(path: str) -> str:
    date = os.path.split(path)[-1]
    file_path = os.path.join(path, f'sales_{date}.json')
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(path, f'sales_{date}-{counter}.json')
        counter += 1
    return file_path

