from projet_tutore_part_1_1 import *


def case_valide(plateau, i, j):
    
    return indice_valide(plateau, i) and indice_valide(plateau, j)

    plateau ={'n':4,
        'cases': [
                    0,0,0,0,   
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0
                ]
}
print(case_valide(plateau,3,0),"doit retourner True")
print(case_valide(plateau,5,2),"doit retourner False")
