import random
import os
import sys

#Initialisation des variables
solution = [0,0,0,0]
tour = 0
bons = 0

print("==============")
print("  Mastermind")
print("==============\n\n")
print("Quatre chiffres différents compris entre 1 et 8\n")

#Génération

nombres = list(range(1,9))

for i in range(0,4):
  rand = random.randint(0,7-i)
  solution[i] = nombres[rand]
  nombres[rand] = nombres[7-i]

#Tour

while(bons != 4):

  
  bons = 0
  mauvais = 0

  tour+=1
  print("Tour "+str(tour))
  essai = input("Entrez une combinaison : ")
  
  #Verification
  
  for i in range(4):
    if(essai[i] == str(solution[i])):
      bons+=1
    else:
      for j in solution:
        if essai[i] == str(j):
          mauvais+=1
          break
        
      
  print(str(bons) + " bien placés et " + str(mauvais) + " mal placés\n")
	

print("Bravo !")

os.system("pause")