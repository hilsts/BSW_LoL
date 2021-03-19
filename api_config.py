import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API']['key']

HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "{API_KEY}".format(API_KEY=API_KEY)
    }

def create_request(url):

    request = requests.get(url, headers=HEADER)

    return request