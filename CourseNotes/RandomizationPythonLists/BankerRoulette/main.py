import random
# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

#  Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")  # Rich, Sam, Ben
names = namesAsCSV.split(", ")
# Don't change the code above

# My code below this line
# print(names)  # ['Rich', 'Ben', 'Sam']
# print(names[0])  # Rich

# print(len(names))  # 3

num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# print(random_choice)

# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to by the meal today!")  # Rich is going to by the meal today!

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to by the meal today!")  # Sam is going to by the meal today!
