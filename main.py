import time
import load_config
import threading

from requests_html import HTMLSession
from events_utils import *
from club_event import ClubEvent
from events_list import EventsList
from discord import send_webhook


def make_request():
	session = HTMLSession()
	page = session.get("https://ithaca.campuslabs.com/engage/organization/open-mic-night/events")
	page.html.render()
	all_events_html = page.html.find("#org-event-discovery-list", first=True)
	if all_events_html == None:
		raise ValueError("No events found.")
	events = generate_dictonary(all_events_html.text)
	
	return events

def start_request_loop():
	all_events = EventsList()
	keep_looping = True
	print("press ctrl-c to stop")
	while True:
		try:
			events_json = make_request()
			all_events.refresh_list(events_json)
			all_events.print_events()
			all_events.send_webhooks()
		except ValueError:
			print("Error Making Request.")

		print("Sleeping...")
		time.sleep(10)


def main():
	load_config.init()
	start_request_loop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit(0)
