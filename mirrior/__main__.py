import argparse
import interpreter
import pointer
import utils

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog = "mirrior", exit_on_error=False)
  parser.add_argument("-run")

  args = parser.parse_args()
  
  if args.run != None:
    try:
      with open(args.run, "r") as file:
        ftext = file.read()
      pntr = pointer.pointer(ftext)
      interpreter.run(pntr, {}, [])
    except FileNotFoundError:
      utils.generalError("cannot find file '" + args.run + "'", "mirrior: error")