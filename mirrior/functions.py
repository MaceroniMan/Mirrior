import utils

# modulos top 2 elements of stack
# outputs the result of modulo
def mod(stack, pos):
  if len(stack) >= 2:
    return [stack.pop(0) % stack.pop(0)]
  else:
    utils.error(pos, "modulo function needs at least 2 items in stack", "stack error")

# prints the top element of the stack
# outputs nothing
def out_pop(stack, pos):
  if len(stack) >= 1:
    print(stack.pop(0))
    return stack
  else:
    utils.error(pos, "print function needs at least 1 item in stack", "stack error")

# prints the top element of the stack
# outputs what is just printed
def out(stack, pos):
  if len(stack) >= 1:
    print(stack[0])
    return stack
  else:
    utils.error(pos, "out function needs at least 1 item in stack", "stack error")

fctns = {
  "mod" : mod,
  "print" : out_pop,
  "out" : out
}

def call(fname, stack, pos):  
  if fname in fctns:
    # call function
    rvalue = fctns[fname](stack, pos)
    
    return rvalue
  else:
    return False