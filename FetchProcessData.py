import requests
import json


class CustomProcessFetcher:
    def __init__(self, bearer_token, url):
        self.bearer_token = bearer_token
        self.url = url

    def fetch_custom_process(self, scenario_id):
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        params = {
            'scenarioId': scenario_id
        }
        response = requests.get(self.url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()["customization"]["parameters"]
            table = {}
            for item in data:
                alias = item["alias"]
                table[alias] = {
                    "options": [],
                    "unit": item.get("unitOfMeasure"),
                    "current value": item.get("value")
                }

                options = item.get("options")
                if options is None:
                    continue
                for option in options:
                    table[alias]["options"].append(option.get("label"))
                    if option.get("value") == item.get("value"):
                        table[alias]["current value"] = option.get("label")
            return table
        else:
            return response.status_code


