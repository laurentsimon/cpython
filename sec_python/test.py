# import os, sys, inspect
# import argparse, traceback, sys, errno
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)


# def main(options):
#     print("title:", options.title)

# def readOptions():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-t', "--title", required=True, default="", help="Title")
#     args = parser.parse_args()
#     return args

# if __name__ == '__main__':
		
# 	args = readOptions()

# 	try:
# 		main(args)
		
# 	except:
# 		#log.exception("exception caught")
# 		traceback.print_exc(file=sys.stdout)
# 	#finally:
# 		#print 'finally'

# 	print('Done ...')

import mymodule, mymodule2, mymodule3



# def do_something_nasty():
#     return requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
if __name__ == '__main__':
	
	#do_something_nasty()
	print("main")
	mymodule.say_hello()
	mymodule.do_one()

	mymodule3.do_one()
	mymodule2.do_one()



