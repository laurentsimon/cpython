import mymodule2

def say_hello():
    print( 'Hello, world!' )
    mymodule2.say_hello2()

def do_one():
    print( 'do_one' )
    mymodule2.do_one()
    do_two()

def do_two():
    print( 'do_two' )  
    mymodule2.do_two()

def do_three():
    print( 'do_three' )  