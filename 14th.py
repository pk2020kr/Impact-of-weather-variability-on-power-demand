row = int(input())               # no. of row increases by one _ _ because we are adding 1 in range 
for i in range(row + 1):
    print (' * '*(i+1) + ' _ '*2*(row-i) + ' * '*(i+1))
    
    