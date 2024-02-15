from requests_html import HTMLSession
from datetime import date, datetime
from event import Event

def month_to_num(month: str):
	month = month.lower()
	match month:
		case "january":
			return 1
		case "february":
			return 2
		case "march": 
			return 3
		case "april":
			return 4
		case "may":
			return 5
		case "june":
			return 6
		case "july":
			return 7
		case "august":
			return 8
		case "september":
			return 9
		case "october":
			return 10
		case "november":
			return 11
		case "december":
			return 12

def convert_to_24_hour_time(date: str):
	split_date = date.split(":")
	if "PM" in date:
		return f"{str(int(split_date[0])+12)}:{split_date[1][:-2]}"
	elif "AM" in date:
		if int(split_date[0]) != 12:
			return date[:-2]
		return f"00:{split_date[1][:-2]}"
	else:
		raise ValueError("Invalid date input.")

def convert_date(text: str):
	
	split_text = text.split(" ")
	split_text = split_text[1:-1]
	del split_text[2]
	split_text[2] = convert_to_24_hour_time(split_text[2])
	split_text[0] = month_to_num(split_text[0])

	# If a future event has a lesser month it has to be next year.
	today = datetime.now()
	if today.month > split_text[0]:
		year = today.year + 1
	else: year = today.year
	split_text = [year] + split_text
	
	output = ""
	for text in split_text:
		output += f"{text}-"
	output = output[:-1]
	return output




def convert_text_to_list(text: str):
	list_text = []
	while "\n" in text:
		index = text.find("\n")
		list_text.append(text[:index])
		text = text[index+1:]
	return list_text

def print_events(events):
	for date, event in events.items():
		print(f"""Name: {event["name"]}\nDate: {date}\nLocation: {event["location"]}\n\n""")


def clean_up_data(data: list):
	club_names_to_remove = ["Ithaca College Nerf Club", "Ithaca College Humans Vs Zombies Social Club", "Hosted by 2 organizations", "Open Mic Night"]
	# Clean up the data to remove the ended text.
	filter_func = lambda line: ("Ended" not in line or "ago" not in line) and line not in club_names_to_remove
	filtered_data = list(filter(filter_func, data))

	# 0: Name
	# 1: Date
	# 2 Location
	events = {}
	for i in range(0, (len(filtered_data))-3, 3):
		date = convert_date(filtered_data[i+1])
		events[date] = {"name": filtered_data[i], "location": filtered_data[i+2]}

	print_events(events)
		



def make_request():
	session = HTMLSession()
	#page = session.get("https://ithaca.campuslabs.com/engage/organization/ithaca-college-nerf-club/events?showpastevents=true")
	page = session.get("https://ithaca.campuslabs.com/engage/organization/open-mic-night/events")
	page.html.render()
	all_events = page.html.find("#org-event-discovery-list", first=True)
	if all_events == None:
		raise ValueError("No events found.")
	clean_up_data(convert_text_to_list(all_events.text))
			

def main():
	make_request()
	
main()	