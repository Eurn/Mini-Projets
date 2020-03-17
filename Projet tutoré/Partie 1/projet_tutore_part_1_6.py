from projet_tutore_part_1_1 import *
from projet_tutore_part_1_2 import *
from projet_tutore_part_1_3 import *
from projet_tutore_part_1_4 import *
from projet_tutore_part_1_5 import *


def affichage_f (plateau):
    n=plateau['n']
    t=plateau['cases']
    lignes=0
    while lignes < n:
        s=''
        colonnes=0
        while colonnes < n:
            s+=str(t[lignes*n+colonnes])+' '
            colonnes+=1
        lignes+=1
        print(s)
    return s



x=creer_plateau(8)
  

affichage_f (x)
