# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("Welcome to Python Pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# My code below this line

bill = 0

if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final is ${bill}")