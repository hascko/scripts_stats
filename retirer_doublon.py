#!/usr/bin/env python3

# On récupère le contenu du fichier good_mail

def del_doublon():
	s = list()
	with open("all_mails", "r") as all_mails:
		# On supprime les doublons du fichier
        	for line in all_mails:
                	if line.strip("\n") and line not in s:
                        	s.append(line)
	        all_mails_str = ''.join(s)

	with open("test4", "w") as test4:
		# On écrit la modification
		test4.write(all_mails_str)	

	with open("all_mails", "w") as all_mails:
        	# On écrit la modification
		all_mails.write(all_mails_str)
