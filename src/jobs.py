import csv

from functools import lru_cache


@lru_cache
def read(path):

    with open(path, encoding="utf-8") as csv_file:
        reader_dict = csv.DictReader(csv_file, delimiter=";", quotechar='"')

        jobs_list = list(reader_dict)

        return jobs_list
