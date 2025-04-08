print("------------------IZIFIN TECHNOLOGY---------------")
exp = int(input("Years of experience:"))
age = int(input("Years of experience:"))

if exp > 25 and age >= 55:
    atr = f"N{5600000.00}"
elif exp > 20 and age >= 45:
    atr = f"N{4480000.00}"
elif exp>10 and age >= 35:
    atr = f"N{1500000.00}"
else:
     atr = f"N{550000.00}"

print(atr)
    


