# Perform addition
def add(x,y):
    return x+y
# Perform subtraction ex.
def subtract(x,y):
    if(x<y):
        return x-y
# Perform multiplication
def multiply(x,y):
    result=x*y
    return result    
# Perform division
def divide(x,y):
    #division implementation 
    if(y==0):
        return Divide_by_0_error
    return x/y
def square(x):
    return x*x