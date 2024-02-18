# from datetime import datetime
import requests

# print(datetime.now())


response = requests.get("https://github.com")
if response.status_code == 200:
    print("Github is up")
