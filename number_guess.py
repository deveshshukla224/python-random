#guessed_number = int(input("Enter a number : "))
count=0
while(count<3):
    guessed_number = int(input("Enter a number : "))
    if(guessed_number==9):
        print("You win")
        count=3
    else:
       count += 1
       if(count==3):
           print("You have reached your limit")