import requests

# response = requests.delete("http://localhost:8080/items/1")
response = requests.get("http://localhost:8080/items")
actual = len(response.json())
expected = 4
assert expected == actual
