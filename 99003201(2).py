import datetime
import calendar
import sys
import re


class age():
    def cal_age(self):
        birth_year = int(input("Enter your year of birth: "))
        birth_month = int(input("Enter your month of birth: "))
        birth_day = int(input("Enter your day of birth: "))
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        current_day = datetime.date.today().day
        age_year = current_year - birth_year
        age_month = abs(current_month-birth_month)
        age_day = abs(current_day-birth_day)
        print("Your age is: ", age_year, "Years", age_month,
              "months and", age_day, "days\n")


class cal_end(age):
    def __init__(self):
        pass

    def entire_year(self):
        yy = int(input("enter year: "))
        print(calendar.calendar(yy))
        print(" ")


class new_cal():
    def month_year(self):
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
        # display the calendar
        print(" ")
        print(calendar.month(yy, mm))


class new_cal2(new_cal, cal_end):
    def week_day(self):
        date = str(input("Enter the date(for example:09 02 2019) : "))
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
        day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        print(day_name[day])
        print("\n")


class new_cal3(new_cal2, age):
    def leap_year(self):
        year = int(input("Enter a year: "))
        # Here, you take the input from the user
        if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
            print("{0} is a leap year!!\n".format(year))
        else:
            print("{0} is not a leap year!!\n".format(year))


cal_obj = new_cal3()
print("Welcom..!")
while(1):
    print("Please Select your Option")
    print("1.Printing the Entire year")
    print("2.Printing the month of the year")
    print("3.Printing the day")
    print("4.Checking leap year or not")
    print("5.Calculate age")
    print("0.Exit")

    n = int(input("Enter your option: "))
    if n == 1:
        cal_obj.entire_year()
        print(re.match("[a-z]{3}", "cal_obj.entire_year"))

    elif n == 2:
        cal_obj.month_year()
        print(re.search("[a-z][1 2]", "cal_obj.month_year"))

    elif n == 3:
        cal_obj.week_day()
        print(re.match("[a-z]", "cal_obj.week_day"))

    elif n == 4:
        cal_obj.leap_year()
        print(re.findall("[1 4]", "cal_obj.leap_year"))

    elif n == 5:
        cal_obj.cal_age()
        print(re.findall("[a-z]", "cal_obj.cal_age"))

    elif n == 0:
        sys.exit()
    else:
        print("Invalid option")
        print("Try again")
    print("\n")
