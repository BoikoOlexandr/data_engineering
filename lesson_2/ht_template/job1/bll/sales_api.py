import os

import requests

from lesson_2.ht_template.bin.check_jobs import create_or_clean_dir
from lesson_2.ht_template.job1.dal import local_disk, sales_api



def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    create_or_clean_dir(raw_dir)
    data = sales_api.get_sales(date=date)
    local_disk.save_to_disk(json_content=data, path=raw_dir)


