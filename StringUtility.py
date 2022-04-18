class StringUtility:
  
  def __init__(selfie, pstr):
    selfie.string = pstr
    print(pstr)

  def __str__(selfie):
    return selfie.string
    
  def vowels(selfie):
    vowels = "aeiouAEIOU" 
    count = 0
    for i in selfie.string:
      if i in vowels:
        count += 1
    if count >= 5:
      return "many"
    return str(count)  

  def bothEnds(self):
    """creates a new sring using the first and last 2 leters
    args: self(self)
    return: (mystring) new string"""
    if len(self.string) <= 2:
      return ""
    else: 
      mystring = self.string[0:2] + self.string[-2:]
      return mystring
      
  def fixStart(selfie):
    """creates a modified string where all occurenes of the args: (self)self"""
    fix = ""
    if len(selfie.string) <= 1:
      return str(selfie.string)
    else: 
      firstcharacter = selfie.string[0]
      for i in selfie.string[1:]:
        if i == firstcharacter:
          fix = fix + "*"
        else: 
          fix += str(i)
      return str(firstcharacter) + str(fix)

def asciiSum(self):
  """Return an integer that is the sum of all ascii values in the string.
  return: (sum) sum of ASCII values"""
  sum = 0
  for i in self.string:
    sum += ord(i)
  return sum


def cipher(self):
  mystring = ""
  alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
  shift = len(self.string)
  for i in self.string:
    if i in alpha:
      char = chr(order(i)+shift)
      if ord(char) >=91:
        while ord(char) >= 91 and i.isupper():
          char = chr(ord(char) - 26)
        while ord(char_ >= 123 and i.islower()):
          char = chr(ord(char) - 26)
      else: 
        char = i
      mystring += char
  return mystring