import requests
import json
request = requests.get("https://random-word-api.herokuapp.com/word?number=5")
print(request.json())
