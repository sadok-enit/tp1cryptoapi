from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
TOKEN = os.environ.get("TOKEN_KEY")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '40',
    'limit': '1',
    'convert':'USD',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY ,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
    print("hello")
    print("testing if CI pipeline workedd")
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
