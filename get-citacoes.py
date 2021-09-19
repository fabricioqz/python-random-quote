def MyFirstCodeTest1():

  f = open("citacoes.txt")
  citacoes = f.readlines()
  f.close()
  print (citacoes)

if __name__== "__main__":
  MyFirstCodeTest1()