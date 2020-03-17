def indice_valide(plateau, indice):
    
    return indice>=0 and indice < plateau['n']



plateau ={'n':4,
        'cases': [
                    0,0,0,0,   
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0
                ]
}


print(indice_valide(plateau, 32),"doit retourner False")
print(indice_valide(plateau, 1),"doit retourner True")

