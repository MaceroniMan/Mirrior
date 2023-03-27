import random
import utils

# prints the top element of the stack and pops stack
# outputs nothing
def out_pop(stack, pntr):
  if len(stack) >= 1:
    print(stack.pop(-1))
    return stack
  else:
    utils.error(pntr, "print function needs at least 1 item in stack", "stack error")
    
# prints the top element of the stack does not pop stack
# prints a newline
def out(stack, pntr):
  if len(stack) >= 1:
    print(stack[-1], end="", flush=True)
    return stack
  else:
    utils.error(pntr, "out function needs at least 1 item in stack", "stack error")

# modulos top 2 elements of stack
# outputs the result of modulo
def mod(stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    try:
      rvalue = first % second
    except TypeError:
      utils.error(pntr, "subtract function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    stack.append(rvalue)
    return stack
  else:
    utils.error(pntr, "modulo function needs at least 2 items in stack", "stack error")
    
# adds the top two elements of the stack
# outputs the result
def add(stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    try:
      rvalue = first + second
    except TypeError:
      utils.error(pntr, "add function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    stack.append(rvalue)
    return stack
  else:
    utils.error(pntr, "add function needs at least 2 items in stack", "stack error")

# subtracts the top two elements of the stack
# outputs the result
def subtract(stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    try:
      rvalue = first - second
    except TypeError:
      utils.error(pntr, "subtract function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    stack.append(rvalue)
    return stack
  else:
    utils.error(pntr, "subtract function needs at least 2 items in stack", "stack error")

# multiplies the top two elements of the stack
# outputs the result
def multiply(stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    try:
      rvalue = first * second
    except TypeError:
      utils.error(pntr, "multiply function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    stack.append(rvalue)
    return stack
  else:
    utils.error(pntr, "multiply function needs at least 2 items in stack", "stack error")

# divides the top two elements of the stack
# outputs the result
def divide(stack, pntr):
  if len(stack) >= 2:
    second = stack.pop(-1)
    first = stack.pop(-1)
    try:
      rvalue = first / second
    except TypeError:
      utils.error(pntr, "divide function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    stack.append(rvalue)
    return stack
  else:
    utils.error(pntr, "divide function needs at least 2 items in stack", "stack error")

# copies the top element of the stack
# outputs the result
def copy(stack, pntr):
  if len(stack) >= 1:
    stack.append(stack[-1])
    return stack
  else:
    utils.error(pntr, "divide function needs at least 2 items in stack", "stack error")

# shift the top x elements of the stack (x is top element of stack)
# outputs the result
def shift_right(stack, pntr):
  if len(stack) >= 1:
    shiftnum = stack.pop(-1)
    if len(stack) >= shiftnum:
      p = stack[-shiftnum:]
      return stack[:-shiftnum] + p[1:] + p[:1]
    else:
      utils.error(pntr, "shift function needs at least '" + str(shiftnum) + "' more items in stack", "stack error")
  else:
    utils.error(pntr, "shift function needs at least 1 item in stack", "stack error")

# shift the top x elements of the stack (x is top element of stack)
# outputs the result
def shift_left(stack, pntr):
  if len(stack) >= 1:
    shiftnum = stack.pop(-1)
    if len(stack) >= shiftnum:
      p = stack[-shiftnum:]
      return stack[:-shiftnum] + p[-1:] + p[:-1]
    else:
      utils.error(pntr, "shift function needs at least '" + str(shiftnum) + "' more items in stack", "stack error")
  else:
    utils.error(pntr, "shift function needs at least 1 item in stack", "stack error")

# adds the length of the stack to the stack
# NOTE: does not include added value
def length(stack, pntr):
  stack.append(len(stack))
  return stack

# pops the top 2 items of the stack
# then makes a random number between items
def rand_int(stack, pntr):
  if len(stack) >= 2:
    try:
      second = stack.pop(-1)
      first = stack.pop(-1)
      stack.append(float(random.randint(first, second)))
      return stack
    except TypeError:
      utils.error(pntr, "randint function cannot be used with both '" + utils.stringtype(first) + "' and '" + utils.stringtype(second) + "'", "type error")
    except ValueError:
      utils.error(pntr, "randint function bad range", "type error")
  else:
    utils.error(pntr, "randint function needs at least 2 items in stack", "stack error")

# prompts the user for a input
# does auto-type converting to int, float and then str
def prompt(stack, pntr):
  inpt = input("")
  try:
    stack.append(float(inpt))
  except ValueError:
    stack.append(str(inpt))
  return stack

# delete the top item of the stack
def delete(stack, pntr):
  if len(stack) >= 1:
    stack.pop(-1)
    return stack
  else:
    utils.error(pntr, "delete function needs at least 1 item in stack", "stack error")

# turns the top item of the stack into a string
# returns the stack
def stringify(stack, pntr):
  if len(stack) >= 1:
    before = stack.pop(-1)
    stack.append(str(before))
    return stack
  else:
    utils.error(pntr, "stringify function needs at least 1 item in stack", "stack error")

# turns the top item of the stack into a string
# returns the stack
def numify(stack, pntr):
  if len(stack) >= 1:
    before = stack.pop(-1)
    try:
      stack.append(float(before))
    except ValueError:
      utils.error(pntr, before + " value cannot be converted to a float datatype", "stack error")
    return stack
  else:
    utils.error(pntr, "numify function needs at least 1 item in stack", "stack error")

class fcaller(object):
  def __init__(self):
    self.fctns = {
      "mod" : mod,
      "print" : out_pop,
      "out" : out,
      "add" : add,
      "subtract" : subtract,
      "multiply" : multiply,
      "divide" : divide,
      "copy" : copy,
      "shiftright" : shift_right,
      "shiftleft" : shift_left,
      "len" : length,
      "in" : prompt,
      "randint" : rand_int,
      "del" : delete,
      "str" : stringify,
      "num" : numify
    }

  def call(self, name, stack, pntr):
    if name in self.fctns:
      # call function
      rvalue = self.fctns[name](stack, pntr)
      
      return rvalue
    else:
      utils.error(pntr, "function name does not exist", "name error")