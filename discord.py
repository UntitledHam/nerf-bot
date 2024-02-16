import requests
import tomllib	
import load_config

def send_webhook(content: dict):
	content = format_embed(content)
	url = load_config.config["webhook_url"]

	result = requests.post(url, json=content)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print(f"Webhook delivered successfully, code {result.status_code}.")

def format_embed(content: dict):
	role_id = load_config.config["role_id"]
	content["content"] = content["content"].format(role_id)

	content["embeds"][0]["color"] = int(content["embeds"][0]["color"][1:], 16)

	return content
