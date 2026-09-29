import requests

response = requests.get("https://mateuszhaldas.com/blog")

print(response.text)
