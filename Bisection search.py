x=435
# this is not working for x>0 and x<1
if(x<=1):
    high=1
else:
    high=x
low=0
guess=0
epsilon=0.00001
num_guess=0
while(abs(guess**2-x)>=epsilon):
    if(guess**2<x):
        low=guess
    else:
        high=guess
    guess=(high+low)/2.0
    num_guess+=1

print("no of guess",num_guess)
print("squre root for number x using bisection search ",guess)