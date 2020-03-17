from projet_tutore_part_1_1 import *
from projet_tutore_part_1_2 import *

def get_case(plateau, i, j):
    
        assert plateau['cases'][i*plateau['n']+j]<=plateau['n']**2
        return plateau['cases'][i*plateau['n']+j]
    
    
    
    
plateau ={'n':4,
        'cases': [
                    0,0,0,0,   
                    0,0,0,0,
                    0,0,0,0,
                    0,2,0,0
                 ]
}
    
    
print(get_case(plateau, 3, 1),"doit retourner 2")
print(get_case(plateau, 0, 0),"doit retourner 0")
