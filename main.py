import time
import load_config
import threading
import traceback

from requests_html import HTMLSession
from events_utils import *
from club_event import ClubEvent
from events_list import EventsList
from discord import send_webhook


def make_request():
	session = HTMLSession()
	page = session.get(load_config.config["url_to_scrape"])
	page.html.render()
	all_events_html = page.html.find("#org-event-discovery-list", first=True)
	if all_events_html == None:
		raise ValueError("No events found.")
		print("No events found.")
	print(all_events_html.text)
	events = generate_dictonary(all_events_html.text)
	
	return events

def start_request_loop():
	all_events = EventsList()
	while True:
		try:
			events_json = make_request()
			all_events.refresh_list(events_json)
			all_events.print_events()
			all_events.send_webhooks()
		
		except Exception:
			traceback.print_exc()
			print("No events found.")
		

		print("Sleeping...")
		time.sleep(load_config.config["sleep_time"])


def main():
	load_config.init()
	start_request_loop()

if __name__ == '__main__':
	main()
