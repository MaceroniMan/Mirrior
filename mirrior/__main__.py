import interpreter
import pointer
import functions
import utils

import sys
import argparse

# note: the stack of the program is as follows:
# the end of the stack list is the top of the stack

if __name__ == "__main__":
  args = sys.argv[1:]

  parser = argparse.ArgumentParser(prog='mirrior')
  parser.add_argument("filename", type=str, help="the mirrior file to be run")
  parser.add_argument("--stacksize", nargs="?", default=1024, help="the maximum stack size", type=int, dest="stacksize")
  parser.add_argument("--maxloop", nargs="?", default=999, help="the maximum times a loop can run without any action", type=int, dest="maxloop")

  args = parser.parse_args()
  
  try:
    with open(args.filename, "r") as file:
      ftext = file.read()
  except FileNotFoundError:
    print("error: file does not exist")
    sys.exit(0)

  pntr = pointer.pointer(ftext, args.maxloop)
  try:
    interpreter.run(pntr, {}, [], functions.fcaller(), args.stacksize)
  except KeyboardInterrupt:
    print("\r", end="")
    utils.error(pntr, "", "keyboard interrupt")