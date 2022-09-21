import sys, os
import myhooks

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

if len(sys.argv) < 1:
    print("missing argument")
    os.exit(-1)

print("running", sys.argv[1])
run(sys.argv[1])