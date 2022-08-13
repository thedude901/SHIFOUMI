#bin/bash

#

#  ____ __     __  _____     _            __          __
# |  _ \\ \   / / |  __ \   | |         /\\ \        / /#
# | |_) |\ \_/ /  | |  | |  | |        /  \\ \  /\  / / #
# |  _ <  \   /   | |  | |  | |       / /\ \\ \/  \/ /  #
# | |_) |  | |    | |__| |_ | |____  / ____ \\  /\  /   #
# |____/   |_|    |_____/(_)|______|/_/    \_\\/  \/    #
#
#
#                                                       
       
#PART 1
import random 
import os
import time
os.system('clear')

print("""



   _____  _    _  _____  ______  ____   _    _  __  __  _____ 
  / ____|| |  | ||_   _||  ____|/ __ \ | |  | ||  \/  ||_   _|
 | (___  | |__| |  | |  | |__  | |  | || |  | || \  / |  | |  
  \___ \ |  __  |  | |  |  __| | |  | || |  | || |\/| |  | |  
  ____) || |  | | _| |_ | |    | |__| || |__| || |  | | _| |_ 
 |_____/ |_|  |_||_____||_|     \____/  \____/ |_|  |_||_____|
                                                              
                                                              
_____________

PIERRE:  1
_________
FEUILLE: 2
_________
CISEAUX: 3
____________






	""")










shifoumi = {1 :'pierre', 2:'feuille', 3:'ciseaux'}
r= random.randint(1,3)
Enteria = r

def lejeu(Enterj):


	####PIERRE
	if Enterj == 1:
		if Enteria == 2:
			print("Vous avez perdu :)")
		elif Enteria == 3:
			print("Vous avez gagner ")
		else:
			print("Egalite!!!")
	####FEUILLE
	if Enterj == 2:
		if Enteria == 3:
			print("Vous avez perdu :)")
		elif Enteria == 1:
			print("Vous avez gagner ")
		else:
			print("Egalite!!!")

	## CISEAUX
	if Enterj == 3:
		if Enteria == 1:
			print("Vous avez perdu :)")
		elif Enteria == 2:
			print("Vous avez gagner ")
		else:
			print("Egalite!!!")		

	else:
		print("Vous n'avez pas respecte les regles!!!")		
b = True
while b :
	Enterj = int(input("VEUILLEZ SELECTIONNEZ(1, 3):\n :"))
	lejeu(Enterj)
	continu = input("Voulez Vous continuer\nOUI(1)/NON(2) :")
	if continu == 1:

		continue
	elif continu == 2:
		print("A PLUS ;P......")
		time.sleep(4)
		b = False	


