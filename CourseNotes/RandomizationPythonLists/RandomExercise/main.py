import random


# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Don't change the code above

# My code below this line
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")



# randomIntegeter = random.randint(1, 10)
# print(randomIntegeter)

# randomFloat = random.random() * 5
# print(randomFloat)

