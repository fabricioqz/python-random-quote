import random
def MyFirstCode():
 #print ("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print (quotes[random])

if __name__== "__main__":
  MyFirstCode()