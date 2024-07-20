import calendar
 
year = 2023
 
for month in range(1, 13):
    num_days = calendar.monthrange(year, month)[1]
    print(f"{calendar.month_name[month]} {year}: {num_days} days")
