from club_event import ClubEvent
class EventsList:
	def __init__(self):
		self.all_events = {}
			
		

	def remove_past_events(self):
		for date, event in self.all_events.items():
			if event.days_from_today() < 0:
				del self.all_events[date]


	
	def refresh_list(self, new_events_json):			
		for date, event in new_events_json.items():
			if date not in self.all_events:
				self.all_events[date] = ClubEvent(event)
		self.remove_past_events()

		

		
		