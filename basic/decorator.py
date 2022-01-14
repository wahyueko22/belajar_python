def five():
    return 5

def add(param):
    return param + param

def func_as_param(func, x):
    return func(x)

five = five()
func_add = func_as_param(add,five)
print("output : ", func_add)

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer()  # returns the nested function

print_msg("hallo")


def print_msg_closure(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function

clos = print_msg_closure("hallo closure")
clos()


def make_decorated(func):
    def inner(*args, **kwargs):
        print("I got decorated")
        for arg in args: 
            print("Argument via *args :", arg) 
        print(kwargs.get('firstname'))
        func()
    return inner

@make_decorated
def original():
    print("I am original")


original("hallo", firstname="john")
