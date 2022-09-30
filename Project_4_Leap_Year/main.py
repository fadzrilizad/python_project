from subprocess import call


year = int(input("Which year do you want to check? "))

# calculate leap year function
def calLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year."
            else:
                return "Not Leap Year."
        else:
            return "Not Leap Year."
    else:
       return "Not Leap Year."

# print result
print(calLeapYear(year))