# modulos top 2 elements of stack
# outputs the result of modulo
def mod(stack):
  return [stack[0] % stack[1]]

# prints the top element of the stack
# outputs nothing
def out_pop(stack):
  print(stack[0])
  return []

# prints the top element of the stack
# outputs what is just printed
def out(stack):
  print(stack[0])
  return stack

fctns = {
  "mod" : [2, mod],
  "print" : [1, out_pop],
  "out" : [1, out]
}

def call(fname, stack):
  fstack = []
  
  if fname in fctns:
    # create a local stack for the function
    for i in range(fctns[fname][0]):
      fstack.append(stack.pop(-1))

    # call function
    rvalue = fctns[fname][1](fstack)
    
    if rvalue != None:
      stack = rvalue + stack
      return stack
    else:
      return False
      
  else:
    return False