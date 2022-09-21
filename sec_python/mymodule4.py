
import sys, requests
def say_hello4():
    # print( 'Hello, world! - 3' )
    # module2 = sys.modules["mymodule2"]
    # module1 = sys.modules["mymodule"]
    #module2.do_one = module1.do_three
    #module2.do_one = say_hack
    # module2.do_one = lambda: print("bla")
    # sys.modules["mymodule2"] = module2
    requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

def say_hack():
    print("hacked func")