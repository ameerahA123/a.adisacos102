print("......SIMPLE INTEREST, COMPOUND INTEREST AND ANNUITY PLAN CALCULATOR...... ")
def inputs():
    global input_1
    input_1 = input("To calculate Simple Interest enter A \n"
      "To calculate Compound Interest enter B \n"
      "To calculate Annuity Plan enter C ")

def input_2():
    global p,r,t,n
    p = int(input("Enter Principal,P"))
    r = int(input("Enter Rate,R"))
    t = int(input("Enter Time,T"))
    n = int(input("Enter the number of times the interest is compounded per year"))


def calculation():

    if input_1 == "A":
        a = p * (1.0 + (r / 100.0) * t)
        interest = a - p
        print(f"Your simple interest: {interest}")

    elif input_1 == "B":
        a = p * (1.0 + (r / n) ** (n*t))
        interest = a - p
        print(f"Your compound interest: {interest}")

    elif input_1 == "C":
        pmt = float(input("Enter the annuity payment (PMT): "))
        a = pmt * (1.0 + (r / n)**(n * t) - 1.0)/(r / n)
        interest = a - p
        print(f"Your annuity plan: {a}")

inputs()
input_2()

while input_1 in ["A", "B", "C"]:
    calculation()

    answer = input("Do you want to continue (Y/N)")
    if answer  == "Y":
        inputs()

    else:
        print("Exiting calculator. Goodbye!")












