import json
import os
from typing import List, Dict, Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    page = 1
    result = []
    while True:
        try:
            print(f"Getting page {page}")
            sales = get_sales_page(date, page)
            page += 1
            result.extend(sales)
        except ValueError:
            break

    return result

def get_sales_page(date: str, page: int=2) -> List[Dict[str, Any]]:
    url = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'
    payload = {'date': date, 'page': page}
    headers = {'Authorization': AUTH_TOKEN}
    res = requests.get(url=url, params=payload, headers=headers)
    if res.status_code == 404 and "You requested page that doesn't exist" in res.text:
        raise ValueError("Invalid page number")
    elif res.status_code != 200:
        raise Exception(f"API returned unexpected status code {res.text} status code {res.status_code}")

    return json.loads(res.content)

if __name__ == '__main__':
    print(get_sales('2022-08-09')[0])