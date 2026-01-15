from datetime import datetime
import re

birthdateinput = input("Enter the bithdate in the format of YYYY/MM/DD : ")

birthdate = re.match('^\d{4}/\d{2}/\d{2}$', birthdateinput)

if birthdate :
    print("Validation successfull")
    year, month, day = map(int, birthdateinput.split("/"))
    dob = datetime(year, month, day)
    today = datetime.today()

    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    print("Age is : " , age)
    
else:
    print("Validation unsuccessfull")