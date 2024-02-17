import requests
import tomllib	
import load_config
from datetime import datetime
from club_event import ClubEvent

def send_webhook(event: ClubEvent, type):
	match type:
		case "discovered": 
			event.has_been_sent["discovered"] = True
		case "n-days": 
			event.has_been_sent["n-days"] = True
		case "today": 
			event.has_been_sent["today"] = True
	content = load_config.config["webhook_format"]
	content = format_embed(content.copy(), event)
	url = load_config.config["webhook_url"]

	result = requests.post(url, json=content)

	try:
		result.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print(f"Webhook delivered successfully, code {result.status_code}.")

	load_config.init()

def format_embed(content: dict, club_event):
	role_id = load_config.config["role_id"]
	username = load_config.config["username"]

	content["username"] = username

	# Sets the role id to @mention in the content part of the message.
	content["content"] = content["content"].format(role_id)
	# Sets the color of the embed.
	content["embeds"][0]["color"] = hex_to_num(content["embeds"][0]["color"])
	content["embeds"][0]["title"] = content["embeds"][0]["title"].format(club_event.name)
	club_event_time = club_event.date_object.strftime("%m-%d-%Y %I:%M%p")

	content["embeds"][0]["description"] = content["embeds"][0]["description"].format(club_event.name, club_event.location, club_event_time)


	return content


def hex_to_num(hex_color):
    # Remove '#' if present
	hex_color = hex_color.lstrip('#')
    
    # Convert hexadecimal color code to decimal values for R, G, and B components
	r = int(hex_color[0:2], 16)
	g = int(hex_color[2:4], 16)
	b = int(hex_color[4:6], 16)
    
    # Combine the decimal values into a single long number
	num = (r << 16) + (g << 8) + b
    
	return num