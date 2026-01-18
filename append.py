data = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(f"{data}\n")

with open("output.txt", "a") as file:
    file.write("Learning file handling in Python.\n")

with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())

