"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    process_subject_info()
    #data = load_data(FILENAME)
    #print(data)
    #process_subject_info()


def process_subject_info():
    subject_data = load_subject_info(FILENAME)
    for info in subject_data:
        print(f"{info[0]} is taught by {info[1]:12} and has {info[2]:3} students")


def load_subject_info(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_info = []
    for line in input_file:
       # print(line)  # See what a line looks like
       # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
       # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
       # print(parts)  # See if that worked
       # print("----------")
        subject_info.append(parts)
    input_file.close()
    return subject_info




main()