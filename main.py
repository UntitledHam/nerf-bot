from requests_html import HTMLSession
from events_utils import *
from club_event import ClubEvent


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
	#make_request()
	test_json = {"name": "Test Nerf Event!", "date": "2024-02-15-19:30", "location": "The Pub @ IC Square"}
	print(test_json)
	test_event = ClubEvent(test_json)

	print(test_event.date_object.strftime("%Y-%m-%d-%H:%M"))
	print(test_event.days_from_today())
main()	