import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)
data = response.json()
print("Random Cat Fact")
print("Fact:", data["fact"])
with open("api_output.txt", "w") as file:
    file.write(data["fact"])
print("Output saved in api_output.txt")
