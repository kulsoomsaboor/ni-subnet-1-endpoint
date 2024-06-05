import requests
import json

url = "http://135.181.63.160:8010/text-to-text"

payload = json.dumps({
  "roles": [
    "system",
    "user"
  ],
  "messages": [
    "Write an essay of 100 words on marine life",
    "Write an essay of 100 words on marine life"
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
