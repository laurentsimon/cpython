
import mymodule4 
def say_hello3():
    print( 'Hello, world! - 3' )

def do_one():
    print( 'do_one - 3' )
    do_two()

def do_two():
    print( 'do_two - 3' )  
    mymodule4.say_hello4()