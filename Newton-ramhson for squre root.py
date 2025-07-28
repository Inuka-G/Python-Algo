x=89435345345
guess=x/2
epsilon=0.001
num_guess=0
while(abs(guess**2-x)>epsilon):
    guess = guess - (((guess**2) - x)/(2*guess))
    num_guess+=1

print("no of guess",num_guess)
print("squre root for x",guess)