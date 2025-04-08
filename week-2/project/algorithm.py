name_1 = input("Enter you name:")
age_1 = int(input("Enter you age:"))

name_2 = input("Enter you name:")
age_2 = int(input("Enter you age:"))

names = []
ages = []

ages.append(age_1)
ages.append(age_2)

names.append(name_1)
names.append(name_2)

print(f"Name: {names[0]}, Age: {ages[1]}")
print(f"Name: {names[1]}, Age: {ages[0]}")