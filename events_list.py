from club_event import ClubEvent
from discord import send_webhook
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


	def send_messages():
		for date, event in self.all_events:
			if event.days_from_today == 3:
				#send_webhook()
				raise ValueError("Not implemented Yet")
			elif event.days_from_today == 1:
				raise ValueError("Not implemented Yet")



		

		
		