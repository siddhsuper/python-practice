import random

# Randomrange is int in between 2 nos
random_num = random.randrange(1, 30)
print(random_num)

# Random is float
random_float = random.random()
print(random_float)

head_tail = random.randint(0, 2)
if head_tail == 1:
    print("its head")
else:
    print("its tail")
