import utils
import copy

def operator(op, stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    rv = None
    if op == "==":
      rv = not first == second
    elif op == "=!":
      rv = not first != second
    elif op == "=<":
      rv = not first < second
    elif op == "=>":
      rv = not first > second
    elif op == "=%":
      rv = not (first % second == 0)
    elif op == "=<<":
      rv = not first <= second
    elif op == "=>>":
      rv = not first >= second
    else:
      utils.error(pntr, "invalid operator", "value error")
    return rv
  else:
    utils.error(pntr, "compare operators need at least 2 values in stack", "stack error")

# sets up so that it will have skipped one character
def skipnextchar(pntr):
  pntr.allowchange = False
  char = pntr.next()
  
  while char == " ":
    char = pntr.next()

  pntr.allowchange = True

def run(pntr, variables, stack, functions):
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

    if len(stack) > 999:
      utils.error(pntr, "stack cannot exceed 999 values", "stack error")

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
        stack = functions.call(recordfunc, stack, pntr)
        recordfunc = None
      else:
        recordfunc += char
        skip = True

    elif recordopt != None:
      recordopt += char
      if recordopt in ["==", "=!", "=<", "=>"]:
        jumpnextchar = operator(recordopt, stack, pntr)
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
          utils.error(pntr, "variable does not exist", "name error")
      elif char == "=": # set var
        if len(stack) >= 1:
          variables[recordvar] = stack.pop(-1)
          recordvar = None
          skip = True # this ends the variable
        else:
          utils.error(pntr, "must have 1 item in the stack to set variable", "stack error")
      elif char == "+": # if number will increment by 1
        try:
          variables[recordvar] += 1
          recordvar = None
          skip = True # this ends the variable
        except:
          utils.error(pntr, "variable is invalid type", "type error")
      elif char == "-": # if number will deincrement by 1
        try:
          variables[recordvar] -= 1
          recordvar = None
          skip = True # this ends the variable
        except:
          utils.error(pntr, "variable is invalid type", "type error")
      elif char in utils.alphabet + "_":
        recordvar += char
        skip = True
      else:
        utils.error(pntr, "not a variable operator", "syntax error")

    elif recordnumber != None:
      if char in utils.numbers:
        recordnumber += char
        skip = True
      elif char == ".":
        if not "." in recordnumber:
          recordnumber += "."
          skip = True
        else:
          utils.error(pntr, "invalid number", "value error")
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
        stack = functions.call("print", stack, pntr)
      elif char == "+":
        stack = functions.call("add", stack, pntr)
      elif char == "-":
        stack = functions.call("subtract", stack, pntr)
      elif char == "*":
        stack = functions.call("multiply", stack, pntr)
      elif char == "%":
        stack = functions.call("divide", stack, pntr)
      elif char == ")":
        stack = functions.call("shiftright", stack, pntr)
      elif char == "(":
        stack = functions.call("shiftright", stack, pntr)
        
      elif char == "[":
        beforedirection = copy.deepcopy(pntr.direction)
        beforeposition = copy.deepcopy(pntr.pos)
        pntr.direction = "left"
        
        stack, variables = run(pntr, variables, stack, functions)
        
        pntr.direction = beforedirection
        pntr.pos = beforeposition
      elif char == "]":
        beforedirection = copy.deepcopy(pntr.direction)
        beforeposition = copy.deepcopy(pntr.pos)
        pntr.direction = "right"
        
        stack, variables = run(pntr, variables, stack, functions)
        
        pntr.direction = beforedirection
        pntr.pos = beforeposition
      elif char == ";":
        return stack, variables # end the 'signal'
      elif char in utils.numbers + ".":
        recordnumber = char
      elif char in utils.alphabet + "_":
        recordvar = char
      else:
        if char != " ": # null char
          utils.error(pntr, "invalid character", "syntax error")