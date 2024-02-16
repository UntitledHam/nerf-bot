import requests
import tomllib	
from load_config import config

def send_webhook(content: dict):

	url = config["webhook_url"]

	result = requests.post(url, json = content)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print(f"Webhook delivered successfully, code {result.status_code}.")