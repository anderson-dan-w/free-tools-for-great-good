import requests

URL = "https://raw.githubusercontent.com/anderson-dan-w/free-tools-for-great-good/master/README.md"
response = requests.get(URL)
print(response.text)
