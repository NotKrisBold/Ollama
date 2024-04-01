import requests
import json

from flask import Flask


url = "http://localhost:30226/api/v1/scenario-template/65e9deeaac492b3a8ae29419"


bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTIwODk2NDcsImlhdCI6MTcxMTQ4NDg0NywianRpIjoiNDkyOTc0YzMtYTJmNy00NGNkLTlhOWYtNTI2Y2E4NzRjNTkwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.k2qKImdEtEjoOReQo6ZcQD1RVkihy9_Fb7j1WTM3WFAIaWn8B2pH6pVDS4-UlH-OoBSEm6Tx7jaSa6ms5YH3bqp-SQW390B3ygS8u0GoR4RoXMNnfKllqf5EOGI-EvAw8eFjl0KRcuc-V_D7zF_hvKam6Z5I8OONiA1JoPzsAkgsgY9dGrD5tfjU5DoX1QO5YL8KCfpdQNA1ov2KAGrjT2QZRWOeTGIsmUnAbl3dx8wil_q4ZLRj32ciqg9OI9HCciV_fwfuCBI6yI1MrJYwsrg3YfPAtQ-kvVzOmg6dX18cSoGFqzL6Qv2rw1NFCkMR6p5ywtRwoQiQTe0CBWpglg"


headers = {"Authorization": f"Bearer {bearer_token}"}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        print("Response content:")
        print(json.dumps(response_json, indent=4))
    else:
        print(f"Request failed with status code: {response.status_code}")

except Exception as e:
    print("An error occurred:", e)
