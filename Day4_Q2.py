age = int(input("Enter the age : "))

if age < 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


#lambda expression

a = lambda x : "Eligible" if int(x) > 18 else "Not Eligible" 
print(a(intput("Enter the age : ")))
