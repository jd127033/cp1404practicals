for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for a in range(0, 110, 10):
    print(a, end=' ')
print()

# b.
for e in range(20, 0, -1):
    print(e, end=' ')
print()

# c.
accumulation = 0
star_count = (int(input("Number of stars: ")))
for u in range(1, (star_count + 1), 1):
    accumulation = u
print("*" * accumulation)

# d.
number_of_stars = (int(input("Please Input the number of incrementing start lines you desire: ")))
for n in range(1, (number_of_stars + 1), 1):
    print("*" * n)
print()
