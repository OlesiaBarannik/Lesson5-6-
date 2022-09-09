import random

range_numbers = []
i = 0
while i < 10:
    i += 1
    range_numbers.append(random.randint(-100, 100))
print ("The greatest number is", max(range_numbers))



