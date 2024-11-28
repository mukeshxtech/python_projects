print("Welcome to rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        print(f"Child tickets are ₹20")
        bill = 20
    elif 12 < age <=18:
        print(f"Youth tickets are ₹30")
        bill = 30
    else:
        print(f"Adult tickets are ₹40")
        bill = 40

    wants_photo = input("Do you want to have a photo take? type y for yes and n for no ")
    if wants_photo == 'y':
        # Add ₹10 to their bill
        bill += 10
    print(f"Your finale bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
