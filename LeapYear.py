import numpy as np

def dayUpperBound(month,year):
        if month in [1, 3, 5, 7, 8, 10, 12] == True:
                upperBound = 31
        elif month != 2:
                upperBound = 30
        elif leapYear(year) == True:
                upperBound = 29
        else:
                upperBound = 28
        return upperBound

def leapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
	return False
	
def main():
	
	#Year input validation
	correctInput = False
	while correctInput != True:
		year = int(input("Enter the target year: "))
		if year < 1900 or year > 2100:
			print("Sorry, that input is invalid. Enter a year between 1900 and 2100")
		else:
			correctInput = True
		
	print("")
		
	#Month input validation
	correctInput = False
	while correctInput != True:
		month = int(input("Enter the target month (numerically): "))
		if month < 1 or month > 12:
				print("Sorry, that input is invalid. Enter a month between 1 and 12")
		else:
			uBound = dayUpperBound(month, year)
			correctInput = True
			
	print("")
			
	#Date input validation
	correctInput = False
	while correctInput != True:
		day = int(input("Enter the target day: "))
		if day < 1 or day > uBound:
			print("Sorry, that input is invalid. Enter a date between 1 and", uBound)
		else:
			correctInput = True
			
	print("")
	
	#Previous day calculation
	inputDate = str(day) + "/" + str(month) + "/" + str(year)
	
	if day == 1:
		if month == 1:
			year = year - 1
			month = 12
			day = 31
		else:
			month = month - 1
			day = dayUpperBound(month, year)
	else:
		day = day - 1
			
	previousDay = str(day) + "/" + str(month) + "/" + str(year)
	
	print("The inputted date was", inputDate, "and the date of the day before that is", previousDay)
	
#main()
