from flask import Flask, jsonify
import fetchData1,fetchExectute1
from FetchProcessData import CustomProcessFetcher
app = Flask(__name__)

# Assuming df is defined and contains the DataFrame you want to serve
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTI4Mzg2MjcsImlhdCI6MTcxMjIzMzgyNywianRpIjoiMGY0MDE5NjItOTBjOS00MDI1LTgxMDEtMTQ0NTY5MzAyYTJhIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiIwYjBhZmExZC1lM2JlLTRmYTMtOWRjOC0zNmNjMjNkZTE1OWYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.PZPgIv7VK5cNrFaxEW1m-E_eEvQx9Z9FZzsT7oJOeHbRPBEt80YkDTqo45NwEYPF8_kmhGo0Jk3e6uvXSsKQmcXAoeYDpCntjsSKEJNr0gcaV2PI7IUqCK7WSviX5lKxn4XzzH1792F2jGArCAR-Uzm50d6I0XWScu4UNiRJZBkxTL5P5ZzVYGFNpdjLkz5FrDOhaygpuiz1J7e-k4i2gBb6dXhcY8SfRFIYZrrYRjQ98mgJWk8vgp5RmeVs3hsLRJHKLFvlavTGawzHWmAXq1JOV_4PW0xv3jg4sZeb3tZC711EbCII7RVqlpbYt3VYBBcxPYBv7IWWImus_oDX8Q"
url = 'http://localhost:30226/api/v1/customized-process/fec0fde6-eca3-44c0-a5d3-e992eb727948'

custom_process_fetcher = CustomProcessFetcher(bearer_token, url)

@app.route('/fetchData', methods=['GET'])
def get_table_data():
    data = custom_process_fetcher.fetch_custom_process('fec0fde6-eca3-44c0-a5d3-e992eb727948')
    return jsonify(data)

@app.route('/fetchExecute', methods=['GET'])
def get_table_execute():
    data = fetchExectute1.fetchExectute1()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
