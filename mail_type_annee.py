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
	lia = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[-2:])
                y = "".join(y)
                lia.append(y)

        z = {}
        while lia:
                a = lia.count(lia[0])
                z[lia[0]] = a
                i = lia[0]
                lia = [y for y in lia if y != i]
        v = sorted(z)

        for g in v:
                for key in z.keys():
                        if g == key:
                                print("L'année ",key,", il y a eu ",z[key]," bon mail(s)")

# Fonction compte les spams par jour dans all_spams

def spam_mail():
	f = open('/home/hassane/all_spams')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
	lia = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[-2:])
                y = "".join(y)
                lia.append(y)

        z = {}
        while lia:
                a = lia.count(lia[0])
                z[lia[0]] = a
                i = lia[0]
                lia = [y for y in lia if y != i]
        v = sorted(z)

        for g in v:
                for key in z.keys():
                        if g == key:
                                print("L'année ",key,", il y a eu ",z[key]," spam(s)")
