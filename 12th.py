a = bool(123)
print(a) # 
print(type(a))

a = bool(0)
print(a)
print(type(a))
a = bool(-245)
print(a)

a = bool(None)    #    bool( 0, 0.0, None, '' ,"")           False 
print(a)







def burger_maker():
    print("Need 2 buns")
    print("Add cheese")
    print("Add patty")
    print("Add Sauces")
    print("Burger is ready")
    

def pizza_maker():
    print("Need pizza base")
    print("Add cheese")
    print("Add Mushrooms")
    print("Add onion")
    print("Pizza is ready")
    

# Orders are coming

# Pizza
pizza_maker()
print()
# Burger
burger_maker()
print()
# Pizza
pizza_maker()
print()
# Burger
burger_maker()

