from datetime import date, datetime

class ClubEvent:
	def __init__(self, event_json):
		self.event_json = event_json
		self.name = event_json["name"]
		self.date_string = event_json["date"]
		self.date_object = timestamp_datetime = datetime.strptime(self.date_string, """%Y-%m-%d-%H:%M""")
		self.location = event_json["location"]
		
		self.has_been_sent = {"discovered": False, "n-days": False, "today": False}

	def days_from_today(self):
		return (self.date_object - datetime.today()).days
			
