idade_gabriel = 18
acertou = False
while acertou == False:
  chute = int(input("chute a idade do Gabriel: "))
  if chute > idade_gabriel :
      print ("Não sou tão velho assim")
  elif chute < idade_gabriel :
      print ("Não sou tão novo assim")
  elif chute == idade_gabriel :
      acertou = True
      print ("Você acertou")
