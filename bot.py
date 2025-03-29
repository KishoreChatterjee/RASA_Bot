import requests

response = requests.post(
    "http://localhost:5005/webhooks/rest/webhook",
    json={"sender": "user", "message": "Hello"}
)

print(response.json())
