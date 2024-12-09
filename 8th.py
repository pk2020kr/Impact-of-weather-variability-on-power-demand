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



# Check if given number is prime
# print "PRIME" or "NOT PRIME" 
n = 32
is_prime = True

for number in range(2,n):
    if n%number==0:
        print("NOT PRIME")
        is_prime = False
        break

if is_prime==True:
    print("PRIME")
    
    