import requests
import json

URI= "https://dbnube-3b225-default-rtdb.firebaseio.com/personas.json"

response = requests.get(URI)

print(f"RESPONSE: {response}")
print(f"RESPONSE: {response.text}")


data = {
    "005":
        {
            "nombre":"Carthoris",
            "email":"carthoris@email.com"
         }
}

print(f"DATA: {data}")
response = requests.patch(URI,json.dumps(data))

print(f"RESPONSE: {response}")

