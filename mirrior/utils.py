import sys
import os

# variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
opts = "=><!"

def error(pntr, message, etype):
  position = pntr.pos
  line = "".join(pntr.program[position[1]])
  print(etype + " at [" + str(position[0]+1) + ", " + str(position[1]+1) + "]: ")
  print("  " + line)
  print("  " + "~"*(position[0]) + "^" + "~"*(len(line.rstrip())-position[0]-1))
  print(message)
  sys.exit(0)

def stringtype(value):
  if isinstance(value, str):
    return "string"
  elif isinstance(value, int):
    return "int"
  elif isinstance(value, int):
    return "float"

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")