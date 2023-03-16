total = 0
total_1 = 0

for n in range(0, 101):
    if n % 2 == 0:
        total += n

for n in range(0, 101, 2):
    total_1 += n

print(total)
print(total_1)
