from date_functions import *
import load_config

def convert_text_to_list(text: str):
	list_text = []
	while "\n" in text:
		index = text.find("\n")
		list_text.append(text[:index])
		text = text[index+1:]
	return list_text


def generate_dictonary(data):
	data = convert_text_to_list(data)
	club_names_to_remove = load_config.config["club_names_to_remove"]
	# Clean up the data to remove the ended text.
	filter_func = lambda line: ("Ended" not in line or "ago" not in line) and line not in club_names_to_remove
	filtered_data = list(filter(filter_func, data))

	# 0: Name
	# 1: Date
	# 2 Location
	events = {}
	for i in range(0, (len(filtered_data)), 3):
		date = convert_date(filtered_data[i+1])
		events[date] = {"name": filtered_data[i], "date": date, "location": filtered_data[i+2]}
	print(events)

	return events		