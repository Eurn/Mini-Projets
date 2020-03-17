from projet_tutore_part_1_1 import *
from projet_tutore_part_1_2 import *
from projet_tutore_part_1_3 import *
from projet_tutore_part_1_4 import *
from projet_tutore_part_1_5 import *
from projet_tutore_part_1_6 import *


def N_B(tab):
    i=0
    t=[]
    while i<len(tab):
        if tab[i]==0:
            t.append(' ')
        elif tab[i]==1:
            t.append('N')
        elif tab[i]==2:
            t.append('B')
        i+=1
    return t

def ligne_etoile(n):
    if n==4:
        print(29*'*')
    elif n==6:
        print(43*'*')
    elif n==8:
        print(57*'*')
    
        

def affichage_m (plateau):
    n=plateau['n']
    t=N_B(plateau['cases'])
    lignes=0
    ligne_etoile(n)
    while lignes < n:
        s='*  '
        colonnes=0
        while colonnes < n:
            s+=str(t[lignes*n+colonnes])+'   *  '
            colonnes+=1
        print(n*'*      '+'*')
        print(s)
        print(n*'*      '+'*')
        ligne_etoile(n)
        lignes+=1
        



x=creer_plateau(8)
  

affichage_m (x)
