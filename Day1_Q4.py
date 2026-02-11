height = int(input("Enter the number of rows: "))

for row in range(height):             
    for space in range(height - (row+1)):  
        print(" ", end="")
    for star in range((2*row) + 1):      
        print("*", end="")
    print() 