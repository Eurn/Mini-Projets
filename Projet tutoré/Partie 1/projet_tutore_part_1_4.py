from projet_tutore_part_1_1 import *
from projet_tutore_part_1_2 import *
from projet_tutore_part_1_3 import *

def set_case(plateau, i, j, val):
    
    assert val == 0 or val == 1 or val == 2
    plateau['cases'][i*plateau['n']+j] = val 
    return plateau['cases'][i*plateau['n']+j]
    
    
    
        
plateau ={'n':4,
        'cases': [
                    0,0,0,0,   
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0
                 ]
}
    
print(set_case(plateau, 1,1,2),"doit retourner 2") print(plateau['cases'],"doit afficher 2 à la case d'indice 5") # Car 1*4+1=5
    
