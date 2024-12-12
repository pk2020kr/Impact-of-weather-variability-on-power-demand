row = int(input())               # no. of row increases by one _ _ because we are adding 1 in range 
for i in range(row + 1):
    print (' * '*(i+1) + ' _ '*2*(row-i) + ' * '*(i+1))
    
n = 5
for row in range(1,n+1):
    # Space
    for _ in range(n-row):
        print(" ",end="")
    
    stars = 2*row - 1
    # Stars
    for s in range(stars):
        print("*",end="")
    
    print()  