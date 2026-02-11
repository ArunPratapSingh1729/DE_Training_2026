text = input("Enter the input:")

with open("file.txt", "w") as file:
    file.write(text)

print("Data Written into the file successfully")
