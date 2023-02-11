import pointer
import utils
import functions

def operator(op, stack):
  rv = None
  if op == "==":
    rv = not stack.pop(-1) == stack.pop(-1)
  elif op == "=!":
    rv = not stack.pop(-1) != stack.pop(-1)
  elif op == "=<":
    rv = not stack.pop(-1) < stack.pop(-1)
  elif op == "=>":
    rv = not stack.pop(-1) > stack.pop(-1)
  else:
    pass # ERROR: that is not a valid operator
  return rv

# sets up so that it will have skipped one character
def skipnextchar(pntr):
  pntr.allowchange = False
  char = pntr.next()
  
  while char == " ":
    char = pntr.next()

  pntr.allowchange = True

def run(pntr, variables, stack):
  recordstring = None
  recordfunc = None
  recordopt = None
  recordvar = None
  recordnumber = None
  skip = False
  jumpnextchar = False

  while True:
    char = pntr.next()
    if char == None: # if it was mirrored
      continue

    # respond to current records
    if recordstring != None:
      if char == '"':
        stack.append(recordstring)
        recordstring = None
        pntr.allowchange = True # allows mirroring again
        skip = True
      else:
        recordstring += char
        skip = True

    elif recordfunc != None:
      if not char in utils.alphabet:
        stack = functions.call(recordfunc, stack)
        recordfunc = None
      else:
        recordfunc += char
        skip = True

    elif recordopt != None:
      recordopt += char
      if recordopt in ["==", "=!", "=<", "=>"]:
        jumpnextchar = operator(recordopt, stack)
        recordopt = None
        skip = not jumpnextchar
      else:
        skip = True

    elif recordvar != None:
      if char == "?": # get var
        if recordvar in variables:
          stack.append(variables[recordvar])
          recordvar = None
          skip = True # this ends the variable
        else:
          pass # ERROR: variable does not exist
      elif char == "=": # set var
        variables[recordvar] = stack.pop(-1)
        recordvar = None
        skip = True # this ends the variable
      elif char == "+": # if number will increment by 1
        try:
          variables[recordvar] += 1
          recordvar = None
          skip = True # this ends the variable
        except:
          pass # ERROR: invalid type
      elif char == "-": # if number will deincrement by 1
        try:
          variables[recordvar] -= 1
          recordvar = None
          skip = True # this ends the variable
        except:
          pass # ERROR: invalid type
      elif char in utils.alphabet + "_":
        recordvar += char
        skip = True
      else:
        pass # ERROR: invalid character for ending variable

    elif recordnumber != None:
      if char in utils.numbers:
        recordnumber += char
        skip = True
      elif char == ".":
        if not "." in recordnumber:
          recordnumber += "."
          skip = True
        else:
          pass # ERROR: cannot have more that one period
      else:
        if "." in recordnumber: # if float
          stack.append(float(recordnumber))
        else:
          stack.append(int(recordnumber))
        recordnumber = None
        
    # then respond to actual character
    if skip:
      skip = False
    elif jumpnextchar:
      skipnextchar(pntr)
      jumpnextchar = False
    else:
      if char == "!":
        skipnextchar(pntr)
      elif char == "@":
        recordfunc = ""
      elif char == '"':
        pntr.allowchange = False
        recordstring = ""
      elif char == "=":
        recordopt = "="
      elif char == ":":
        stack = functions.call("print", stack)
      elif char == "[":
        pass
      elif char == "]":
        pass
      elif char == ";":
        return stack # end the 'signal'
      elif char in utils.numbers + ".":
        recordnumber = char
      elif char in utils.alphabet + "_":
        recordvar = char
      else:
        if char != " ": # null char
          pass # ERROR: invalid char