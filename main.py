from requests_html import HTMLSession
from events_utils import *


def make_request():
	session = HTMLSession()
	#page = session.get("https://ithaca.campuslabs.com/engage/organization/ithaca-college-nerf-club/events?showpastevents=true")
	page = session.get("https://ithaca.campuslabs.com/engage/organization/open-mic-night/events")
	page.html.render()
	all_events_html = page.html.find("#org-event-discovery-list", first=True)
	if all_events_html == None:
		raise ValueError("No events found.")
	events = generate_dictonary(all_events_html.text)

	print_events(events)
			

def main():
	make_request()

main()	