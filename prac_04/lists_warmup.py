numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] will return the first value within the list which is 3 as lists are indexed starting from 0
# numbers[-1] will return a value of 2 as the indexing will be looped back to the end of the list which has a value of 2
# numbers[3] will return a value of 1 as lists are indexed starting from 0.
# numbers[:-1] will return the list "numbers" minus the final value "2" giving an output of [3, 1, 4, 1, 5, 9]
# numbers[3:4] will return only the elements within the specified index range 3 up until but not including index 4, therefore the output will be [1]
# 5 in numbers will return a value of True as this expression checks if a value is within a list. 5 is within this list so true.
# 7 in numbers will return a value of False as the expression checks if 7 is in the list but it isn't therefore False
# "3" in numbers will return a value of False as this checks for 3 with the type str. The 3 in the list is an integer.
# numbers + [6, 5, 3] will return the list numbers with the addition of [6, 5, 3] to the end of the list. Therefore the output would be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

# Statements to produce altered results
# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:-1])

# Print whether 9 is an element of numbers, not a validation while loop as another input is not intended.
if 9 in numbers == False:
    print("9 is not in the list")
else:
    print("9 is in the list")



