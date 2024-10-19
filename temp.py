

def myFact(n):
    if n == 1:
        return 1
    else:
        return n * myFact(n-1)
    

print(myFact(3))