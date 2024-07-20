import datetime
year = int(input("Enter year: "))
firstday = datetime.datetime(year, 1,1)
print("First Day of ", year, " = ", firstday.strftime("%A"))
