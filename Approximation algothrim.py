# finding square root for x by using approx method

x=2323
guess=0
increament=0.0001
epsilon=0.01
num_guesses=0
while(abs(guess**2-x)>epsilon and guess**2<=x):
    guess+=increament
    num_guesses+=1
    print("number of guesses",num_guesses)

print("number of guesses",num_guesses)
print("is close to square root of",guess)