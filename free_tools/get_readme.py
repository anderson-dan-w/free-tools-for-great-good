import requests

URL = "https://raw.githubusercontent.com/anderson-dan-w/free-tools-for-great-good/master/README.md"


def get_readme():
    response = requests.get(URL)
    return response.text


def get_readme_all_caps():
    text = get_readme()
    return text.upper()
