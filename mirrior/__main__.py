import interpreter
import pointer
import functions

import sys
import json

# note: the stack of the program is as follows:
# the end of the stack list is the top of the stack

def parseEnv():
  try:
    environment = None
    valid = True
    
    with open(".mirrior", "r") as file:
      environment = json.loads(file.read())

    if not "main_file" in environment:
      valid = False

    if valid:
      return environment
    else:
      print("invalid environment")
      sys.exit(0)
  except FileNotFoundError:
    print("no environment created")
    sys.exit(0)

def create():
  environment = {
    "main_file" : ""
  }
  
  print("mirrior environment creator")
  while True:
    fname = input("main file name: ")
    try:
      open(fname)
      environment["main_file"] = fname
      break
    except FileNotFoundError:
      print("that file does not exist")
      continue

  with open(".mirrior", "w") as file:
    file.write(json.dumps(environment))

if __name__ == "__main__":
  args = sys.argv[1:]

  if len(args) == 0:
    environment = parseEnv()

    try:
      with open(environment["main_file"], "r") as file:
        ftext = file.read()
    except FileNotFoundError:
      print("main file does not exist")
      sys.exit(0)
      
    pntr = pointer.pointer(ftext)
    interpreter.run(pntr, {}, [], functions.fcaller())
  else:
    if args[0] == "config":
      pass
    elif args[0] == "create":
      create()
    elif args[0] == "help":
      print("""usage: mirrior [create|help]

commands:
  create ..... used to create the mirrior environment
  help ....... prints this help menu

when ran with no argument, mirrior will run the environment""")