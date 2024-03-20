unit = int(input("Introduce the total of units which you are going to buy:\n"))
unit_cost = int(input("Introduce the cost per unit of the product:\n"))
total = unit_cost*unit
discount10 = total - (total*0.10)
discount5 = total - (total*0.05)
if unit > 10:
    print(f"The total cost of your products is: ${discount10}")
else:
    print(f"The total cost of your products is: ${discount5}")