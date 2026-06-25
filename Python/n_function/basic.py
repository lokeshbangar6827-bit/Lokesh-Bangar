# function are a block of code used to perform specific code(reuseable).
# types of fuction :
# Built in :- already present in python, we can only use,not modify.
            # Example: len(),max(),sum()...etc

# Userdefined:- created by programmer or developer.
            # 1] no return type no argument:
                     # def f_n( ):
            # 2] no return type with argument.
            # 3]with return type without arguments.
                # def grt_no():
                    # return 10**2
                    # 2 ways: var--->store, print(fun()) 


# 1] no return type no argument:

def greet():
    print("Welcome user!")

greet() #function call--> fuction_name()

#  2] no return type with argument:

def greet1(name):
    print("Welcome",name)

name=input("enter yr name: ")    
greet1(name)

# 3] with return type without arguments.

def getno():
    return 10**2

print(getno())

# value use
op=getno()
print(op)
op+=2
print(op)
 