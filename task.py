print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?$"))
tip=float(input("How much tip would you like to give? 10, 12,or 15 :"))
split=int(input("How many people to split the bill? "))
tip*=0.01
tip+=1
total_bill*=tip
total_bill/=split
total_bill=round(total_bill,2)
print(f"Each person should pay:{total_bill}")