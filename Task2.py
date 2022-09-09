import random

range_numbers1 = []
range_numbers2 = []

i = 0
while i < 10:
    i += 1
    range_numbers1.append(random.randint(1, 10))
    range_numbers2.append(random.randint(1, 10))

range_numbers3 = list(set(range_numbers1 + range_numbers2))
print(range_numbers3)


