#!/usr/bin/env python3

def del_lines():
	with open("/home/hassane/all_spams", "r") as test3:
		# On récupère le contenu de test3 pour supprimer les 3 premières lignes
		test3_str = ''.join(test3.readlines()[3:])

	with open("/home/hassane/test4", "w") as test4:
		# On écrit la modification
		test4.write(test3_str) 

	with open("/home/hassane/all_spams", "w") as all_spams:
                # On écrit la modification
                all_spams.write(test3_str)
	print("les trois premières lignes, on bien été retirées")

def del_lignes_vides():
	chaine = r"\n" #Texte à rechercher
	contenu = list()
 
	with open("all_mails", "r") as all_mails:
		for ligne in all_mails:
    			if ligne.strip("\n") and chaine not in ligne:
        			contenu.append(ligne)
	all_mails_str = ''.join(contenu)	
 
	with open("test5", 'w') as test5:
		test5.write(all_mails_str)
	
	with open("all_mails", "w") as all_mails:
                # On écrit la modification
                all_mails.write(all_mails_str)	
