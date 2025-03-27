import numpy as np
option = float(input("To find the root of a quadratic equation, enter 1\n"
      "To find the root of a cubic equation, enter 2\n"
      "To find the root of a quartic equation, enter 3\n"))
if option == 1:
      print("Ax^2 + Bx + C")
      a = float(input("Enter the value of A:"))
      b = float(input("Enter the value of B:"))
      c = float(input("Enter the value of C:"))

      discriminant = b**2.0 - 4.0*a*c
      x1 = (-b + discriminant**0.5)/(2*a)
      x2 = (-b - discriminant ** 0.5) / (2 * a)

      print(f"The first root of your equation is {x1}\n"
            f"The second root of your equation is {x2}")
if option == 2:
      print("Ax^3 + Bx^2 + Cx + D")
      a = float(input("Enter the value of A:"))
      b = float(input("Enter the value of B:"))
      c = float(input("Enter the value of C:"))
      d = float(input("Enter the value of D:"))

      p = float((3 * a * c - b ** 2)/(3 * a ** 2))
      q = float(((2 * b**3) - ( 9 * a * b * c) + (27 * a**2 * d))/(27 * a**3 ))

      root = ((-q/2)+((q/2)**2 + (p/3)**3)**0.5)**(1/3)
      root_1 = (-(q / 2) - ((q / 2) ** 2 + (p / 3) ** 3) ** 0.5) ** (1 / 3)

      roots = root + root_1 - (b / (3 * a))

      print(f"The root of your equation is {roots}")

if option == 3:
      print("Ax^4 + Bx^3 + Cx^2 + Dx + E")
      a = float(input("Enter the value of A:"))
      b = float(input("Enter the value of B:"))
      c = float(input("Enter the value of C:"))
      d = float(input("Enter the value of D:"))
      e = float(input("Enter the value of E:"))

      coefficients = [a, b, c, d, e]
      roots = np.roots(coefficients)

      print(f"The roots of your equation is {roots}")





