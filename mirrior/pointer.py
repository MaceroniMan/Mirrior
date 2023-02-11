import utils

# get a certain character, use pointer[x:y]
# expecting a non-empty program

class pointer(object):
  def __init__(self, program, maxlooping=999):
    self.program = self.splitter(self.whitespace(program))

    # width, height
    self.dims = [len(self.program[0])-1, len(self.program)-1]
    self.pos = [-1, 0] # offset for first character
    self.direction = "right"

    # set to false for strings
    self.allowchange = True

    self.loopingcheck = 0
    self.maxlooping = maxlooping
    
  def next(self):
    if self.direction == "right":
      self.pos[0] += 1
    elif self.direction == "left":
      self.pos[0] -= 1
    elif self.direction == "up":
      self.pos[1] -= 1
    elif self.direction == "down":
      self.pos[1] += 1

    if self.inrange(self.pos[0], self.pos[1]):
      char = self[self.pos[0]:self.pos[1]]
      if char in ["/", "\\", "_",  "|", "{", "}"]:
        if self.allowchange:
          self.loopingcheck += 1
          if self.loopingcheck >= self.maxlooping:
            utils.error(self.pos, "loop repeated over " + str(self.maxlooping) + " times", "loop error")
          self.mirror(char)
          return None # if it was redirected
        else:
          self.loopingcheck = 0
          return char
      else:
        self.loopingcheck = 0
        return char
    else:
      utils.error(self.pos, "pointer tried to access a out of range character", "range error")

  def __getitem__(self, key):
    # key.start: x    key.stop: y
    if self.inrange(key.start, key.stop):
      return self.program[key.stop][key.start]
    else:
      utils.error(self.pos, "pointer tried to access a out of range character", "range error")

  def inrange(self, x, y):
    if y < self.dims[1] and y >= 0:
      if x < self.dims[0] and x >= 0:
        return True
      else:
        return False
    else:
      return False

  def mirror(self, char):
    directions = {
      "/" : {
        "right" : "up",
        "left" : "down",
        "up" : "right",
        "down" : "left"
      },
      "\\" : {
        "right" : "down",
        "left" : "up",
        "up" : "left",
        "down" : "right"
      },
      "|" : {
        "right" : "left",
        "left" : "right",
        "up" : "up",
        "down" : "down"
      },
      "_" : {
        "right" : "right",
        "left" : "left",
        "up" : "down",
        "down" : "up"
      },
      "}" : {
        "right" : "right",
        "left" : "right",
        "up" : "right",
        "down" : "right"
      },
      "{" : {
        "right" : "left",
        "left" : "left",
        "up" : "left",
        "down" : "left"
      },
    }
    self.direction = directions[char][self.direction]

  @staticmethod
  def whitespace(text):
    returntext = ""
    lines = text.split("\n")
    maxline = 0
    
    for line in lines:
      if len(line) > maxline:
        maxline = len(line)

    maxline += 1
  
    for line in lines:
      spacestoadd = maxline-len(line)
      returntext += line + " "*spacestoadd + "\n"
  
    return returntext

  @staticmethod
  def splitter(block):
    returnlist = []
    lines = block.split("\n")
    
    for line in lines:
      currentlist = []
      for ch in line:
        currentlist.append(ch)
      returnlist.append(currentlist)
      
    return returnlist