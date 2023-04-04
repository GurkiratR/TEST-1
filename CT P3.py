def convertSalary(salary, country):
    if country == "Canada":
        convertedSalary = salary * 1.47
        currencyName = "CAD"   
    elif country == "USA":
        convertedSalary = salary * 1.18
        currencyName = "USD"
    elif country == "United Kingdom":
        convertedSalary = salary * 0.91
        currencyName = "Pound Sterling"
    elif country == "Cambodia":
        convertedSalary = salary * 4847.38
        currencyName = "Cambodian riel"
    else:
        print("Error: Invalid country entered.")
        return
    
    if country == "Canada":
        averageSalary = 64000
    elif country == "USA":
        averageSalary = 56516
    elif country == "United Kingdom":
        averageSalary = 35423
    elif country == "Cambodia":
        averageSalary = 5649856
        
    if convertedSalary > averageSalary:
        status = "rich"
    else:
        status = "poor"
        
    print("You will be", status, "in", country, "with a salary of", convertedSalary, currencyName)
    return convertedSalary

salary = float(input("Please enter your salary in Germany: "))
country = input("Enter the country you want to migrate to: ")

convertSalary(salary, country)
