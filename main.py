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
	for i in range(len(events)):
		print(f"""Name: {events[i]["name"]}\nDate: {events[i]["date"]}\nLocation: {events[i]["location"]}\n\n""")


def clean_up_data(data: list):
	# Clean up the data to remove the ended text.
	filter_func = lambda line: ("Ended" not in line or "ago" not in line) and (line != "Ithaca College Nerf Club" and line != "Ithaca College Humans Vs Zombies Social Club" and line != "Hosted by 2 organizations")
	filtered_data = list(filter(filter_func, data))

	# 0: Name
	# 1: Date
	# 2 Location
	events = []
	for i in range(0, (len(filtered_data))-3, 3):
		events.append({"name": filtered_data[i], "date": convert_date(filtered_data[i+1]), "location": filtered_data[i+2]})

	print_events(events)
		



def make_request():
	session = HTMLSession()
	page = session.get("https://ithaca.campuslabs.com/engage/organization/ithaca-college-nerf-club/events?showpastevents=true")
	page.html.render()
	all_events = page.html.find("#org-event-discovery-list", first=True)
	clean_up_data(convert_text_to_list(all_events.text))
			

def main():
	make_request()
	#convert_date("Saturday, November 4 at 1:39PM EDT")

	today = datetime.now()
	print(today.year)	

main()	