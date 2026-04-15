import requests

pl = {
    "name": "Punyak",
    "age": 20,
    "desc": "Backend Dev"
}

print("\nGET Endpoint")
resp1 = requests.get("http://127.0.0.1:8000/status")
print(resp1.status_code)
print(resp1.json())

print("\nPOST Endpoint")
resp2 = requests.post("http://127.0.0.1:8000/register", json=pl)
print(resp2.status_code)
print(resp2.json())