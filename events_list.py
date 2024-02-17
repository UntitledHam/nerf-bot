from club_event import ClubEvent
from discord import send_webhook
import load_config
class EventsList:
	def __init__(self):
		self.all_events = {}
			
		

	def remove_past_events(self):
		for date, event in self.all_events.items():
			if event.days_from_today() < 0:
				del self.all_events[date]


	
	def refresh_list(self, new_events_json):			
		for date, event in new_events_json.items():
			if date not in self.all_events.keys():
				self.all_events[date] = ClubEvent(event)
		self.remove_past_events()


	def print_events(self):
		for date, event in self.all_events.items():
			print(f"""Name: {event.name}\nDate: {event.date_string}\nLocation: {event.location}\n\n""")



	def send_webhooks(self):
		for date, event in self.all_events.items():
			if not event.has_been_sent["discovered"]:
				send_webhook(event, "discovered")
			elif event.days_from_today() == load_config.config["amount_of_days_before_to_notify"] and not event.has_been_sent["n-days"]:
				send_webhook(event, "n-days")
			elif event.days_from_today() == 0 and not event.has_been_sent["today"]:
				send_webhook(event, "today")
			else:
				print("Webhook already been sent, skipping...")



		

		
		