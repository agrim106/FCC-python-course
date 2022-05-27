secret_word = "mister"
guess = " "
guess_count = 0
guess_limit = 3
out_of_tries = False 


while guess != secret_word and not(out_of_tries):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_tries = True
        
         
if out_of_tries:
    print("out of tries, goodluck next time")
else:           
    print("You win")  

