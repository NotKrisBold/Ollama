import requests
import pandas as pd
import json as js

def fetchExectute1():
    # Define your bearer token
    bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTI4Mzg2MjcsImlhdCI6MTcxMjIzMzgyNywianRpIjoiMGY0MDE5NjItOTBjOS00MDI1LTgxMDEtMTQ0NTY5MzAyYTJhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.PZPgIv7VK5cNrFaxEW1m-E_eEvQx9Z9FZzsT7oJOeHbRPBEt80YkDTqo45NwEYPF8_kmhGo0Jk3e6uvXSsKQmcXAoeYDpCntjsSKEJNr0gcaV2PI7IUqCK7WSviX5lKxn4XzzH1792F2jGArCAR-Uzm50d6I0XWScu4UNiRJZBkxTL5P5ZzVYGFNpdjLkz5FrDOhaygpuiz1J7e-k4i2gBb6dXhcY8SfRFIYZrrYRjQ98mgJWk8vgp5RmeVs3hsLRJHKLFvlavTGawzHWmAXq1JOV_4PW0xv3jg4sZeb3tZC711EbCII7RVqlpbYt3VYBBcxPYBv7IWWImus_oDX8Q"

    url = 'http://localhost:30226/api/v1/basic/calculate-scenario'

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    params = {
        'scenarioId': 'fec0fde6-eca3-44c0-a5d3-e992eb727948'
    }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print("bho")

    url = "http://localhost:30226/api/v1/impact-method/6070b11f-e863-486c-9748-14341de36259"

    headers = {
        "Authorization":  f'Bearer {bearer_token}',
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        names = response.json()
    else:
        print("bho")

    data = data[0]["phaseResults"]
    names = names["impactCategories"]
    table = {}
    for item in names:
        table[item["name"]] = {}
    for i in range(0, len(data)):
        for j in range(0, len(data[i]["nodeImpactResult"]["impactList"])):
            for item in names:
                if item["refId"] == data[i]["nodeImpactResult"]["impactList"][j]["refId"]:
                    value_unit = (data[i]["nodeImpactResult"]["impactList"][j]["value"],
                                  data[i]["nodeImpactResult"]["impactList"][j]["unit"])
                    table[item["name"]][data[i]["nodeImpactResult"]["name"]] = value_unit

    df = pd.DataFrame(table)
    df = df.transpose()
    return df.to_dict()
