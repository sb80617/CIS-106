import math
def total(num1, num2):
   total_price = num1 * num2
   if total_price > 100000.00:
       total_price = total_price *.10
   return total_price

def problem_1():
    while True:
        consent = input("Do you want to run program?: ")
        if consent != "Yes" and consent != "yes":
            break
        quantity = round(float(input("Enter quantity purchased: ")),2)
        price = round(float(input("Enter price of good: ")),2)
        total_price = total(price, quantity)
        print(f"Quantity entered: {quantity}")
        print(f"Price entered: {price}")
        print(f"total: {total_price}")
problem_1()

