
range_numbers = list(range(1,100))
range_numbers1 = []
i = 0
while i < len(range_numbers):
    i+=1

    if i % 7 == 0 and i % 5 > 0:
        range_numbers1.append(i)

print(range_numbers1)

