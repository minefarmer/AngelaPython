import random


# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Don't change the code above


# My code below this line
# random.seed(123)  # a random seed will always produce the same number

# random_integar = random.randint(1, 10)
# print(random_integar)

# random_float = random.random() * 5
# print(random_float)


random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")