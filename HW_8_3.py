import requests
from datetime import datetime
import time


class StackoverflowApi:
    def _get_todate(self):
        todate = round(time.time())
        return todate

    def _get_fromdate(self, num_days):
        fromdate = round(self._get_todate() - num_days * 24 * 60 * 60)
        return fromdate

    def print_questions(self, num_days=1, tag=""):
        url = 'https://api.stackexchange.com/2.3/questions/'
        q_questions = 0
        page = 0
        while True:
            page += 1
            params = {
                "site": "stackoverflow",
                "tagged": tag,
                "todate": self._get_todate(),
                "fromdate": self._get_fromdate(num_days),
                "sort": "creation",
                "page": page,
                "pagesize": 100
            }
            response = requests.get(url=url, params=params)
            data = response.json()
            if not data["items"]:
                print('Вопросы закончились')
                break
            for item in data["items"]:
                print(f'{datetime.utcfromtimestamp(item["creation_date"])} - {item["title"]}\n{item["link"]}')
            q_questions += len(data["items"])
            time.sleep(0.5)

        print(f'-----------------------------------------'
              f'\nВсего вопросов с тэгом "python": {q_questions}')


sof = StackoverflowApi()
sof.print_questions(num_days=2, tag="python")
