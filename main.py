print("Welcome to pythin Pizza Deliveries!")
size = input("Which size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0
if size == "S":
    price= 15
    print(f"The price for Small sized Pizza is ${price}")
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    print(f"The price for Small sized Pizza is ${price}")
    if add_pepperoni == "Y":
        price += 3
else:
    price = 25
    print(f"The price for Small sized Pizza is ${price}")
    if add_pepperoni == "Y":
        price += 3

if extra_cheese == "Y":
    price += 1
print(f"Your total bill is ${price}")

