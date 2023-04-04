month = input("Enter the month in numeric form: ")
day = input("Enter the day in numeric form: ")
year = input("Enter the year as two numerical digits (e.g. 98, 20, 21): ")

if not month.isdigit() or int(month) < 1 or int(month) > 12:
    print("Error: Invalid Month Input")
elif not day.isdigit() or int(day) < 1 or int(day) > 31:
    print("Error: Invalid Day Input")
elif not year.isdigit() or len(year) != 2:
    print("Error: Invalid Year Input")
else:
    print(f"{month}/{day}/{year} - Success: Congratulations! you entered the correct date.")
