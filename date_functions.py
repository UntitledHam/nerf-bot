from datetime import date, datetime


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
		