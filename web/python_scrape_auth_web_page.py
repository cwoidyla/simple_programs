import requests
import json
import base64

LOGIN_URL = "https://awesomesite.com/auth/login"

with open("./config.json") as json_data_file:
    cfg = json.load(json_data_file)

USERNAME = cfg['credentials']['username']
PASSWORD = base64.b64decode(cfg['credentials']['password'])

def scrape(url):
    """
    :param url:
    :return dictionary with URL to HTML:
    """
    session_requests = requests.session()
    payload = {
        "name": USERNAME,
        "password": PASSWORD
    }
    # Perform login
    login = session_requests.post(LOGIN_URL,
                                  data = payload,
                                  headers = dict(referer = LOGIN_URL))
    # Scrape url for data
    results = {}
    i = 0
    response = session_requests.get(url, headers = dict(referer = url))
    results[url] = response.content # store raw HTML