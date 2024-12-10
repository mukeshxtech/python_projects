"""Who will pay the bill"""
import random

print("Welcome to bill payer picker")

names = []
count = 0

try:
    total_number_of_people = int(input('For how many people bill has to be paid? '))
    if total_number_of_people < 1:
        print("You have to give the total count of people")
        exit()
except ValueError:
    print("You have to give the total count of people")
    exit()
else:
    while count < total_number_of_people:
        person = input(f"Person {count+1} : ").strip()
        if person == '':
            print("You have to give the person name")
        else:
            names.append(person)
            count += 1

# random_index = random.randint(0,(total_number_of_people-1))
# print(f"{names[random_index]} will pay the bill!")

person_to_pay_the_bill = random.choice(names)
print(f"{person_to_pay_the_bill} will pay the bill!")

