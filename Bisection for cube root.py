x=27
epsilon=0.01
low=0
high=x
guess=0
num_guess=0
while(abs(guess**3-x)>epsilon):
    if(guess**3<x):
        low=guess
    else:
        high=guess
    num_guess+=1
    guess=(high+low)/2
print("no of guess",num_guess)
print("cube root of x",guess)