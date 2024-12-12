x = 20
y = 34
print(x+y)
a = "Hello"
b = "World"
print(a + b)
a = "5.0"
b = float(a)
print(b)
print(type(b))
c = int(b)
print(c)
print(type(c))
bool()
bool('')
bool("")
bool(0)
bool(00)
bool(0.0)
bool(0.00)   # Any no. of zero give False
a = bool(4.9)
print(a)
a = bool(0.0)
print(a)

# str
a = bool("Pranav")
print(a)

# +, -, *, /, **, //, %
print(4+2)
print(4-2)
print(4*2)
print(4**2)  # Expoment
print(4/2)   # Devision
print()
print(4//2)  # in devision after doing //, we can remove after decimel part
print(5/2)
print(5//2)
print(10/3)
print(10//3)
print()
print(4%3)   # Remender


#python work like a logic gets are called logical operator
print (4<2 or 4>2)
print (4<2 and 4>2)
print (not 4>2)
# some need to understand
print (4==2)  #equal
print (4!=2)  #not equal
print (4<=2)  #less then and equal to
print (4>=2)  #greater then and equal to
# show error
#print (4=!2) 
#print (4=<2) 
#print (4=>2)

x = -10

if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')
    
    
n = 15
if n%3==0:
    print("Fizz",end="")
if n%5==0:
    print("Buzz")






n = int(input())

print(" -- For --")
for i in range(n):
    print("*", end=" ")

print()
print(" -- While --")
    
i = 1
while i<=n:
    print("*", end=" ")
    i+=1
    



print('addng from web')


    
    
    


for i in range(4):
    print("*", end="")

print() # default end="\n"
    
for i in range(4):
    print("*", end="")

print("",end="\n")
    
for i in range(4):
    print("*", end="")
    

 
 
 n = 8

for i in range(1,n+1): # outer loop which will go over each row
    # Some code that will print stars
    for j in range(i): # inner loop
        print("*",end="")
    print()

4

# Make this final

n = 10

for i in range(1,n+1):
    # Star1
    for j in range(n-i+1):
        print("*",end="")
        
    # Space
    space = 2*i - 2
    for j in range(space):
        print(" ",end="")
        
    # Star2
    for j in range(n-i+1):
        print("*",end="")
    
    print()


# youtube
def average_grade(marks):
  
  ave=sum(marks)/len(marks)
 
  print('your average mark is ', ave)

  if ave>=80:
    print('A')
  elif ave>=60:
    print('B')
  elif ave>=40:
    peint('c')
  else:
    print('f')
    
    
    

# youtube
def add_number(n1, n2):     # hear n1 , n2  are Formal argument (which is given in def)
  c=n1+n2
  return c

add_number(4,8)             # hear 4 , 8  are Actual argument  ( when you pass the argument) 
                                   # 4 types - - >  Position,   Keyword,   Default,                          Variable Length
#                                                     (4, 8)   (n2=8,n1=4)  write at end of {def line ()}. 

# seen by youtube link https://youtu.be/-Bkupx9gX0o
# def = defination, & inside bracket which is argument, The terms parameter = argument can be used for the same thing: information that are passed into a function. From a
# function's perspective: A parameter is the variable listed inside the parentheses in the function definition.
#  *  An argument is the value that are sent to the function when it is called.
def greed(name):                                                                 # parameter = argument - - - - A value which is supplied to the function to operate on
  print('Hi',name)                                                               
  print('How are you',name,'?')

greed('Ram')       # hear we passed ram as a argument to the greed function

print()# just for spacing

def add_number(n1, n2):
  c=n1+n2
  return c     # return function only assine the value

add_number(4,8)         # hear we passed no. 4 & 6 as a argument to the add_number function

print()# just for spacing

def greed_return(name):
  print('Hi',name)
  return
  print('How are you')

greed_return('Krishna')

