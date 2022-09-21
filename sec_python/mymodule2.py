import mymodule3
def say_hello2():
    print( 'Hello, world! - 2' )

def do_one():
    print( 'do_one - 2' )
    do_two()

def do_two():
    print( 'do_two - 2' )
    mymodule3.do_two()