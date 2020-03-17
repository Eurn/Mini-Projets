from projet_tutore_part_1_1 import *
from projet_tutore_part_1_2 import *
from projet_tutore_part_1_3 import *
from projet_tutore_part_1_4 import *


def creer_plateau(n):
    assert n==4 or n==6 or n==8
    tableau={'n':n,'cases':[]}
    i=0
    while i<n**2:
        tableau['cases'].append(0)
        i+=1
    set_case(tableau, (n//2)-1,(n//2)-1,2)
    set_case(tableau, (n//2)-1,(n//2),1)
    set_case(tableau, (n//2),(n//2)-1,1)
    set_case(tableau, (n//2),(n//2),2)
    return tableau
        
        
        
        
print(creer_plateau(8))
