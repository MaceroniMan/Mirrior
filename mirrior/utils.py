import sys

# variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
opts = "=><!"

def error(position, message, etype):
  print(etype + " at [" + str(position[0]+1) + ", " + str(position[1]+1) + "]: " + message)
  sys.exit(0)