from datetime import datetime
import re

userbirthdate = input("Enter the bithdate in the format of YYYY/MM/DD : ")

try:
    userbirthdate = re.match('^\d{4}/\d{2}/\d{2}$', birthdateinput)

    if userbirthdate :
      user_year,user_month,user_days = map(int , userbirthdate.split("/"))
      current_datetime = datetime.now()
      
      user_age = current_datetime.year - year
    if (current_datetime.month , current_datetime.day) > (user_month ,user.day):
      user_age -= 1
      
    print("The users age is : ", user_age)
except Exception as e:
      print("Exception: ", e)

