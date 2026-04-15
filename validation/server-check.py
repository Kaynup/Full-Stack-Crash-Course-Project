import requests

pl = {
    "first_name":"Punyak",
    "last_name":"User",
    "email":"punyak@test.com",
    "job_title":"Backend Dev",
    "salary":50000
}

print("\nGET Endpoint")
resp1 = requests.get("http://127.0.0.1:8000/status")
print(resp1.status_code)
print(resp1.json())

print("\nPOST Endpoint")
resp2 = requests.post("http://127.0.0.1:8000/register", json=pl)
print(resp2.status_code)
print(resp2.json())