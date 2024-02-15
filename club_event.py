from datetime import date, datetime

class ClubEvent:
	def __init__(self, event_json):
		self.event_json = event_json
		self.name = event_json["name"]
		self.date_string = event_json["date"]
		self.date_object = timestamp_datetime = datetime.strptime(self.date_string, """%Y-%m-%d-%H:%M""")
		self.location = event_json["location"]

	def equals(other_event):
		#if self.name == other_event.name and self.date == other_event.date and self.location == other_event.location:
		#	return True
		#return false
		raise ValueError("Not implemented yet.")

	def isLessThan(other_event):
		raise ValueError("Not implemented yet.")
			
