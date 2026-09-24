import os
import time
import requests

API_KEY = os.environ["MUAPI_API_KEY"]
BASE = "https://api.muapi.ai/api/v1"
headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
payload = {'prompt': 'Transform this samurai cliff scene into a neon cyberpunk style, glowing city skyline in the distance, rain-soaked ground with light reflections.', 'video_url': 'https://example.com/replace-with-your-file'}

response = requests.post(f"{BASE}/runway-aleph-v2v", headers=headers, json=payload, timeout=60)
response.raise_for_status()
request_id = response.json()["request_id"]
print("request_id:", request_id)

while True:
    result = requests.get(f"{BASE}/predictions/{request_id}/result", headers=headers, timeout=60)
    result.raise_for_status()
    data = result.json()
    status = data.get("status")
    if status in ("completed", "failed"):
        print(data)
        break
    time.sleep(3)
