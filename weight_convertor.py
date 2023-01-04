weight = float(input("Please enter you weight: "))
option_opted = input("Please enter entered weight category: L(bs) or Kg  ")
option_lower_case=option_opted.lower()
print(option_lower_case)
if(option_lower_case == "kg"):
    coverted_weight=(weight*2.205)
    print(f'Weight in Pound is {coverted_weight}')
elif(option_lower_case=='lbs'):
    coverted_weight=(weight/2.205)
    print(f'Weight in Kg is {coverted_weight}')
else:
    print("Invalid option opted")
