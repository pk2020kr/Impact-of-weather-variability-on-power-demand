print("Hi, I'm _ _  welcome")  #Python is Case sensitive
print(10 + 10)
print("10")
print("10+10")
#Integers
print(type(5))
#Float
print(type(-5.5))
#Strings
print(type("What's the type for this data"))
#Boolean
print(type(True))



n = 453
sum=0
while n>0:
    rem = n%10 # 453%10 -> 3 | 45%10 -> 5 | 4%10 -> 4
    sum+=n%10
    print(rem, end=" ")
    n = n//10  # 453//10 -> 45 | 45//10 -> 4 | 4//10 -> 0
print()
print(sum)

n = 453
sum=0
while n>0:
    rem = n%10 # 453%10 -> 3 | 45%10 -> 5 | 4%10 -> 4
    sum+=n%10
    print(rem, end=" ")
    n = n//10  # 453//10 -> 45 | 45//10 -> 4 | 4//10 -> 0
print()
print(sum)


print("Step 1")
for i in range(1,7,-2):
    print(i, end=" ")
    
print("Step 2")








