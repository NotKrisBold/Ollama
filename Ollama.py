import requests
import json
import gradio as gr
from fetchExecute2 import ScenarioCalculator
import pandas as pd
from flask import jsonify

bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTIwODk2NDcsImlhdCI6MTcxMTQ4NDg0NywianRpIjoiNDkyOTc0YzMtYTJmNy00NGNkLTlhOWYtNTI2Y2E4NzRjNTkwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJjNjEyMGFlOS1iYjExLTRlMGQtOGFmMi04MGYwMTQwM2VkMzAiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.k2qKImdEtEjoOReQo6ZcQD1RVkihy9_Fb7j1WTM3WFAIaWn8B2pH6pVDS4-UlH-OoBSEm6Tx7jaSa6ms5YH3bqp-SQW390B3ygS8u0GoR4RoXMNnfKllqf5EOGI-EvAw8eFjl0KRcuc-V_D7zF_hvKam6Z5I8OONiA1JoPzsAkgsgY9dGrD5tfjU5DoX1QO5YL8KCfpdQNA1ov2KAGrjT2QZRWOeTGIsmUnAbl3dx8wil_q4ZLRj32ciqg9OI9HCciV_fwfuCBI6yI1MrJYwsrg3YfPAtQ-kvVzOmg6dX18cSoGFqzL6Qv2rw1NFCkMR6p5ywtRwoQiQTe0CBWpglg"
scenario_id = "fec0fde6-eca3-44c0-a5d3-e992eb727948"
impact_method_id = "6070b11f-e863-486c-9748-14341de36259"

calculator = ScenarioCalculator(bearer_token)
result_table = calculator.generate_table(scenario_id, impact_method_id)
df = pd.DataFrame(result_table)
df = df.transpose()
pd.set_option('display.max_columns', None)
print(df)

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}

conversation_history = []


def generate_response(prompt):
    global conversation_history  # declare isInitialized as global
    conversation_history.append(prompt)

    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "greta",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None


iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch()
