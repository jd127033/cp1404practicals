""" Random Practical task Question Answers """
# line 1 print(random.randint(5, 20))
# a: The smallest number that could be printed is 5 as the given range is from 5 to 20.
# b: This code prints a random number within the given range

# line 2 print(random.randrange(3, 10, 2))
# a: The smallest number that could be printed is 3 as this is the beginning of the range
# b: The largest possible number was 9 as the range increments by 2 meaning 10 is not possible given 3 is the smallest number in the range
# c: An output of 4 is impossible as the numbers increment by 2 and the smallest number was 3. The next smallest possible output would be 5.

# line 3 print(random.uniform(2.5, 5.5))
# a: The smallest number possible is 2.5, the largest possible number can be 5.5 but this is dependent on rounding.

import random

# Code to produce a random number within the range of 1 to 100 inclusive
print(random.randint(1, 100))
