print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza you want? S, M or L : ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0

if size == 'S':
    bill += 90
elif size == 'M':
    bill += 200
elif size == 'L':
    bill += 380
else:
    print("Please share the correct input! ")

if pepperoni == 'Y':
    if size =='S':
        bill += 20
    else:
        bill += 30

if extra_cheese == 'Y':
    bill += 10

print(f"Your final bill is : ₹{bill}")
