import requests
import requests.auth
import os
from dotenv import load_dotenv
from plagiarize import parse_word

load_dotenv()
SECRET = os.getenv('SECRET')
APP_ID = os.getenv('APP_ID')
PASSWORD = os.getenv('PASSWORD')
KEY = os.getenv('API-KEY')

# Obtain access token
def authorize():
	client_auth = requests.auth.HTTPBasicAuth(APP_ID, SECRET)
	post_data = {'grant_type': 'password', 'username': 'plagiarize_this', 'password': PASSWORD}
	headers = {'User-Agent': 'plagiarize_this by kevalii'}
	response = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers)
	return response.json()['access_token']


# print(authorize())
# print(parse_word("The unbearable lightness of being by Milan Kundera", KEY))