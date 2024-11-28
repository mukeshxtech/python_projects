print("Welcome to rollercoaster")
height = int(input("What is your height in cm? "))
child_ticket = 20
youth_ticket = 30
adult_ticket = 40

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        print(f"Child tickets are ₹{child_ticket}")
        child_photo = input("Do you want photos? yes or no?")
        if child_photo=='yes':
            print(f"Your total bill is ₹{child_ticket + 10}")
        elif child_photo=='no':
            print(f"Your total bill is ₹{child_ticket}")
        else:
            print("yes or no?")
    elif 12 < age <=18:
        print(f"Youth tickets are ₹{youth_ticket}")
        youth_photo = input("Do you want photos? yes or no?")
        if youth_photo == 'yes':
            print(f"Your total bill is ₹{youth_ticket + 10}")
        elif youth_photo == 'no':
            print(f"Your total bill is ₹{youth_ticket}")
        else:
            print("yes or no?")
    else:
        print(f"Adult tickets are ₹{adult_ticket}")
        adult_photo = input("Do you want photos? yes or no?")
        if adult_photo == 'yes':
            print(f"Your total bill is ₹{adult_ticket + 10}")
        elif adult_photo == 'no':
            print(f"Your total bill is ₹{adult_ticket}")
        else:
            print("yes or no?")
else:
    print("Sorry you have to grow taller before you can ride. ")
