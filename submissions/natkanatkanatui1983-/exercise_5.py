secret = 7
guess = int(input ("Guess the secret number :\n"))
while guess != secret:
    if guess < secret:
        print("Too Low") 
    else:
        print("Too high")
        guess = int(input ("Guess the secret number :\n"))
        print("Correct!")