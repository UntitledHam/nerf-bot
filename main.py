import sys
import os
import time

from requests_html import HTMLSession
from events_utils import *
from club_event import ClubEvent
from events_list import EventsList


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
	while True:
		try:
			events_json = make_request()
			all_events.refresh_list(events_json)
		except ValueError:
			print("Error Making Request.")

		print("Sleeping for 30 Seconds.")
		time.sleep(30)

		

def shutdown():
	print("Make this later lol.")
			

def main():
	start_request_loop()

if __name__ == '__main__':
   main()