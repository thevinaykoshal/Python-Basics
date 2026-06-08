#Compound Interest (Total Amount) = Principal * (1 + Rate/100)^Time
principal=float(input("enter the pricipal value : "))
rate = float (input ("enter the intrest rate : "))
time = float (input("enter the time in months : "))
compound_interest = principal* (1+rate/100)**time
print(f"the total amount after compounding : {compound_interest}")
