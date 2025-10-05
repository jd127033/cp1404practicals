""" Files Practical Task Question Responses """

# a: Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
FILENAME = "name.txt"
name_file = open(FILENAME, 'w')
user_name = input("Please enter your name: ")
print(f"{user_name}", file=name_file)
name_file.close()

# b:
in_file = open(FILENAME)
# reads name in file and strips the trailing next line \n to the right
name = in_file.read().rstrip('\n')
in_file.close()
print(f"Hi {name}!")

# c:
with open("numbers.txt", 'r') as file:
    # extract first and second number
    first_number = file.readline().strip()
    second_number = file.readline().strip()

solution = int(first_number) + int(second_number)
print(solution)

# d:
result = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        #takes number from each line then adds it to the running total
        number = int(line.strip())
        result = result + number
print(result)



