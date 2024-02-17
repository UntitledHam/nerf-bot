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


def convert_to_24_hour(time_str):
	print(time_str)
    # Split the time string into hours, minutes, and AM/PM indicator
	time_str = time_str[:-2] + " " + time_str[-2:]
	print(time_str)
	hours, minutes = time_str[:-2].split(':')
	period = time_str[-2:]
    
    # Convert hours to integer
	hours = int(hours)
    
    # If it's PM and not noon, add 12 hours to convert to 24-hour format
	if period.upper() == 'PM' and hours != 12:
		hours += 12
    
    # If it's AM and it's midnight (12 AM), convert hours to 00
	if period.upper() == 'AM' and hours == 12:
		hours = 0
    
    # Format the time in 24-hour format
	time_24_hour = '{:02d}:{:02d}'.format(hours, int(minutes))
    
	return time_24_hour
	


def convert_date(text: str):
	split_text = text.split(" ")
	split_text = split_text[1:-1]
	del split_text[2]
	split_text[2] = convert_to_24_hour(split_text[2])
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
		