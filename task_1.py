
# def calculateTotalItemsCost(x1:float,x2:float,x3:float):
#     return x1+x2+x3


item1:float = float(input("Kindly enter the cost of first item: "))
item2:float = float(input("Kindly enter the cost of second item: "))
item3:float = float(input("Kindly enter the cost of third item: "))
totalCost:float = item1+item2+item3
print("The total cost of all items is: ", totalCost )
totalBudget:float = float(input("Kindly enter your budget: "))



if totalCost <= totalBudget:
    difference = totalBudget - totalCost
    print(f"You are within budget. You have {difference:.2f} left.")
else:
    difference = totalCost - totalBudget
    print(f"You are over budget. You need an additional {difference:.2f}.")

