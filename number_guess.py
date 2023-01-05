secret_number=9
guess_count=0
guess_limit=3
while(guess_count<guess_limit):
    guessed_number = int(input("Enter a number : "))
    guess_count+=1
    if(guessed_number==secret_number):
        print("You win")
        break
        #immediately break out of loop
else:
    print("You have reached your limit")
#while loop with else - as soon as loop terimates this part gets executed