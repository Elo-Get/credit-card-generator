from random import *

import string
import re

a = 0


print("    ╭─━━━━━─╯ Generateur de cc ╰─━━━━━─╮\n          created by ASIAN_P0WER \n              le 04/10/2020 \n")   #graphisme simple mais rendant le programme un minimum potable visuelement





while a == 0: "boucle pour le programme 
    bincc = int(input("  Entrer le bin de votre choix (6 chiffre) :  "))
    o = 202
    a = 1


    if bincc < 100000 or bincc > 999999: #regarde si le bin est bon ou pas 
        print("   \n Votre bin est trop petit ou trop grands ")   #si differente du schema demandé envoie d'une erreur
        a = 0
    else:   #sinon continu le processus 
        generation = int(input("          nombre de cc a generer : "))     #demande du nombre de cc voulu (1 a infini)
        if generation == 0:      #si la demande = 0 , le programme revient au debut
            print("fin")
            a = 0
            
        else:       #si toutes les conditions sont respecté, genere le nombre de cc demandé 
            
            print("   \n voici les cartes :   \n  ")
            for i in range(generation):
                l = [bincc]
                p = []
                m = []
                r = [o]
                for i in range(10):
                    l.append(randint(0, 9))
                    card = ''.join(str(elem) for elem in l) 
                for i in range(1):
                    m.append(randint(0, 1))
                    mois = ''.join(str(elem) for elem in m)
                    if mois == 0:
                        m.append(randint(1, 9))
                        mois = ''.join(str(elem) for elem in m)
                    elif mois == 1:
                        m.append(randint(0, 2))
                        mois = ''.join(str(elem) for elem in m)
                    else:
                        m.append(randint(1, 2))
                        mois = ''.join(str(elem) for elem in m)
                        
                for i in range(1):
                    r.append(randint(0, 9))
                    annee = ''.join(str(elem) for elem in r)

                for i in range(3):
                    p.append(randint(0, 9))
                    ccv = ''.join(str(elem) for elem in p)

                taxe = card, "|", mois, '|', annee, "|", ccv

                total = "".join(str(elem) for elem in taxe)
                a=0
                


                

                print(total)  #fin de la generation, renvoie le tout
    print("\n")

                
