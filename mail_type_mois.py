#!/usr/bin/env python3

import os

# Fonction qui range et compte les bon mails par jour dans good_mail
def bon_mail():
	os.system("grep \"C=\"250 2.0.0 Ok: queued as\" /home/hassane/all_mails > /home/hassane/good_mail")
	f = open('/home/hassane/good_mail')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
	lim = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[2])
                y = "-".join(y)
                lim.append(y)

        s = {}
        while lim:
                a = lim.count(lim[0])
                s[lim[0]] = a
                i = lim[0]
                lim = [y for y in lim if y != i]
        v = sorted(s)

        for g in v:
                for key in s.keys():
                        if g == key:
                                print("Le mois du ",key,", il y a eu ",s[key]," bon mail(s)")

# Fonction compte les spams par jour dans all_spams

def spam_mail():
	f = open('/home/hassane/all_spams')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
	lim = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[2])
                y = "-".join(y)
                lim.append(y)

        s = {}
        while lim:
                a = lim.count(lim[0])
                s[lim[0]] = a
                i = lim[0]
                lim = [y for y in lim if y != i]
        v = sorted(s)

        for g in v:
                for key in s.keys():
                        if g == key:
                                print("Le mois du ",key,", il y a eu ",s[key]," spam(s)")	
