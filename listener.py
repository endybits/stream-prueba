import requests

user_id = "123"
url = f"http://127.0.0.1:8000/stream/{user_id}"

with requests.get(url, stream=True) as response:
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))