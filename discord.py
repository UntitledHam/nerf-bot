import requests
import tomllib	
import load_config
from datetime import datetime

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

def format_embed(content: dict, club_event):
	role_id = load_config.config["role_id"]

	# Sets the role id to @mention in the content part of the message.
	content["content"] = content["content"].format(role_id)
	# Sets the color of the embed.
	content["embeds"][0]["color"] = int(content["embeds"][0]["color"][1:], 16)

	club_event_time = club_event.date_object

	test_message["embeds"][0]["description"] = test_message["embeds"][0]["description"].format(club_event.name, club_event.location, club_event_time)



	return content
