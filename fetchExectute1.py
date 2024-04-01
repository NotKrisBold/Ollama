import requests
import pandas as pd
import json as js

# Define your bearer token
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTIwODk2NDcsImlhdCI6MTcxMTQ4NDg0NywianRpIjoiNDkyOTc0YzMtYTJmNy00NGNkLTlhOWYtNTI2Y2E4NzRjNTkwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.k2qKImdEtEjoOReQo6ZcQD1RVkihy9_Fb7j1WTM3WFAIaWn8B2pH6pVDS4-UlH-OoBSEm6Tx7jaSa6ms5YH3bqp-SQW390B3ygS8u0GoR4RoXMNnfKllqf5EOGI-EvAw8eFjl0KRcuc-V_D7zF_hvKam6Z5I8OONiA1JoPzsAkgsgY9dGrD5tfjU5DoX1QO5YL8KCfpdQNA1ov2KAGrjT2QZRWOeTGIsmUnAbl3dx8wil_q4ZLRj32ciqg9OI9HCciV_fwfuCBI6yI1MrJYwsrg3YfPAtQ-kvVzOmg6dX18cSoGFqzL6Qv2rw1NFCkMR6p5ywtRwoQiQTe0CBWpglg"


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
                table[item["name"]][data[i]["nodeImpactResult"]["name"]] = data[i]["nodeImpactResult"]["impactList"][j]["value"]

df = pd.DataFrame(table)
df = df.transpose()
pd.set_option('display.max_columns', None)
print(df)

from flask import Flask, jsonify

app = Flask(__name__)

# Assuming df is defined and contains the DataFrame you want to serve


@app.route('/get', methods=['GET'])
def get_table():
    return jsonify(df.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
