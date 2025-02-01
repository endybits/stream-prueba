import requests

def listen_to_stream(user_id):
    url = f"http://127.0.0.1:8000/stream/{user_id}"
    
    with requests.get(url, stream=True) as response:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8').replace("data: ", "")
                print(decoded_line, end="", flush=True)  # Stream output in real-time
                
                if "[END OF STREAM]" in decoded_line:
                    print("\nStream closed.")
                    break  # Exit loop when stream ends

user_id = "123"
listen_to_stream(user_id)