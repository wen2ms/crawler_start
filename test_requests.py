import requests

url = "https://books.toscrape.com"

r = requests.get(url=url)

if r.ok:
    print(r.text)
else:
    print("Request failed!")
