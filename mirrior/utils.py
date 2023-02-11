import sys

# variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
opts = "=><!"
valid = "_"


def error(position, message, etype):
  print(etype + " at [" + str(position[0]) + ", " + str(position[1]) + "]: " + message)
  sys.exit(0)

def generalError(message, etype):
  print(etype + ": " + message)
  sys.exit(0)