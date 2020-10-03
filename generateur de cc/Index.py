from random import *
import string
import re
import Index
a = 0



def generator():
     a = randint(0, 9)
     b = randint(0, 9)   
     c = randint(0, 9)   
     d = randint(0, 9)     
     e = randint(0, 9)   
     f = randint(0, 9)   
     g = randint(0, 9)   
     h = randint(0, 9)   
     i = randint(0, 9)   
     j = randint(0, 9)
     l = (bincc, a, b, c, d, e, f, g, h, i, j)
     re.sub(r"\s+", "", l)
     print(l)   

def erreur1():
    print("fin")
    a = 0

while a == 0:
    
    #demande le bin de la cc pour la generer ( un bin = 6 chiffre)
    bincc = int(input("entrer le bin de votre choix (6 chiffre) : "))
    
    a = 1

    #regarde si le bin est un minimum valide c'est a dire superieur a 100000 mais inferieur a 999999
    if bincc > 100000 and bincc < 999999:
        generation = int(input("nombre de cc a generer : "))
        
        #regarde combien de cc la personne veut generer (minimum 1 max infini)
        if generation == 0:
            erreur1()               #si la personne marque 0 une erreur s'affiche et le programe recommence tous 
        
        else:    #sinon genere le nombre de cc demandé
            
            print(" ")                       
            print("voici les cartes : ")    
            print(" ")
            for i in range(generation):
                generator()
                  

                
                a = 0
    else:                           #si le bin est trop petit une erreur apparait et le programe redemarre
        print("votre bin est trop petit ou trop grands")
        a = 0
