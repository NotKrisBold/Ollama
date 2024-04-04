import requests
import pandas as pd
import json as js

# Define your bearer token
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTI4Mzg2MjcsImlhdCI6MTcxMjIzMzgyNywianRpIjoiMGY0MDE5NjItOTBjOS00MDI1LTgxMDEtMTQ0NTY5MzAyYTJhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.PZPgIv7VK5cNrFaxEW1m-E_eEvQx9Z9FZzsT7oJOeHbRPBEt80YkDTqo45NwEYPF8_kmhGo0Jk3e6uvXSsKQmcXAoeYDpCntjsSKEJNr0gcaV2PI7IUqCK7WSviX5lKxn4XzzH1792F2jGArCAR-Uzm50d6I0XWScu4UNiRJZBkxTL5P5ZzVYGFNpdjLkz5FrDOhaygpuiz1J7e-k4i2gBb6dXhcY8SfRFIYZrrYRjQ98mgJWk8vgp5RmeVs3hsLRJHKLFvlavTGawzHWmAXq1JOV_4PW0xv3jg4sZeb3tZC711EbCII7RVqlpbYt3VYBBcxPYBv7IWWImus_oDX8Q"

url = 'http://localhost:30226/api/v1/customized-process/fec0fde6-eca3-44c0-a5d3-e992eb727948'

headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json; charset=utf-8'
}
params = {
    'scenarioId': 'fec0fde6-eca3-44c0-a5d3-e992eb727948'
}

response = requests.get(url, headers=headers)

table = {}

if response.status_code == 200:
    data = response.json()["customization"]["parameters"]
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

    print(js.dumps(table, indent=4))
else:
    print(response.status_code)

