import interpreter
import pointer
import functions
import utils

import sys

# note: the stack of the program is as follows:
# the end of the stack list is the top of the stack

if __name__ == "__main__":
  args = sys.argv[1:]

  if len(args) == 0:
    print("needs a file name")
  else:
    try:
      with open(args[0], "r") as file:
        ftext = file.read()
    except FileNotFoundError:
      print("file does not exist")
      sys.exit(0)

    pntr = pointer.pointer(ftext)
    try:
      interpreter.run(pntr, {}, [], functions.fcaller())
    except KeyboardInterrupt:
      print("\r", end="")
      utils.error(pntr, "", "keyboard interrupt")