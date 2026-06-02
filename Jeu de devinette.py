import random
def devinette():
  Nombre_secret= random.randint (1,100)
  Tentatives= 0
  Tentatives_max= 5
  print("Bienvenue! Devinez le nombre secret")
  while True:
    Nombre= int(input("Entrez un nombre"))
    Tentatives+=1
    if Nombre == Nombre_secret:
        print("Vous avez gagné !")
        print("Nombre d'essais: ", Tentatives)
        break
    Ecart=abs(Nombre - Nombre_secret)
    if Nombre > Nombre_secret:
        if Ecart <= 10:
         print("C'est trop grand, mais vous êtes presque!")
        else:
          print("C'est trop grand et vous êtes trop loin !") 
        print("Essayez encore")
    elif Nombre < Nombre_secret:
        if Ecart >= 10:
         print("C'est trop petit, mais vous êtes presque!")
        else:
         print("C'est trop petit et vous êtes trop loin !")
         print("Essayez encore")
    if Tentatives==Tentatives_max:
     print("Dommage! Vous avez épuisé vos 5 tentatives")
     print("Le nombre secret était:", Nombre_secret)
devinette()

