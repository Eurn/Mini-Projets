def indice_valide(plateau, indice):
    return indice>=0 and indice < plateau['n']

def case_valide(plateau, i, j):
    return indice_valide(plateau, i) and indice_valide(plateau, j)

def get_case(plateau, i, j):
        assert plateau['cases'][i*plateau['n']+j]<=plateau['n']**2
        return plateau['cases'][i*plateau['n']+j]

def set_case(plateau, i, j, val):
    assert val == 0 or val == 1 or val == 2
    plateau['cases'][i*plateau['n']+j] = val 
    return plateau['cases'][i*plateau['n']+j]

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
        print((n*7+1)*'*')

def afficher_plateau (plateau):
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

def pion_adverse(joueur):
    assert joueur==1 or joueur==2
    if joueur == 1:
        return 2
    return 1

def prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
    if case_valide(plateau,i+vertical,j+horizontal) and get_case(plateau,i+vertical,j+horizontal)==pion_adverse(joueur):
        x=i+2*vertical
        y=j+2*horizontal
        while case_valide(plateau, x, y):
            if get_case(plateau,x,y)==0:
                return False
            elif get_case(plateau,x,y)==joueur:
                return True
            x+=vertical
            y+=horizontal
    return False

def mouvement_valide(plateau,i,j,joueur):
    if get_case(plateau,i,j) == 0:
        if prise_possible_direction(plateau,i,j,0,-1,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,0,1,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,-1,0,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,-1,-1,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,-1,1,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,1,-1,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,1,0,joueur):
            return True
        elif prise_possible_direction(plateau,i,j,1,1,joueur):
            return True

    return False   

def mouvement_direction(plateau,i,j,vertical,horizontal,joueur):
    if prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):
        x=i+vertical
        y=j+horizontal
        while get_case(plateau,x,y)==pion_adverse(joueur):
            set_case(plateau,x,y,joueur)
            x+=vertical
            y+=horizontal     

def mouvement(plateau,i,j,joueur):
    if mouvement_valide(plateau, i, j, joueur):
        set_case(plateau,i,j,joueur)
        mouvement_direction(plateau,i,j,-1,-1,joueur)
        mouvement_direction(plateau,i,j,-1,0,joueur)
        mouvement_direction(plateau,i,j,-1,1,joueur)
        mouvement_direction(plateau,i,j,0,-1,joueur)
        mouvement_direction(plateau,i,j,0,1,joueur)
        mouvement_direction(plateau,i,j,1,-1,joueur)
        mouvement_direction(plateau,i,j,1,0,joueur)
        mouvement_direction(plateau,i,j,1,1,joueur) 

def joueur_peut_jouer(plateau,joueur):
    n=plateau['n']
    i=0
    while i<n:
        j=0
        while j<n:
            if mouvement_valide(plateau,i,j,joueur):
                return True
            j+=1
        i+=1
    return False  

def fin_de_partie(plateau):
    if not joueur_peut_jouer(plateau, 2) and not joueur_peut_jouer(plateau, 1):
        return True
    else:
        return False

def gagnant (plateau):
    tableau=plateau['cases']
    i=0
    compteur1=0
    compteur2=0
    while i <len(tableau):
        if tableau[i]==1:
            compteur1=compteur1+1
        elif tableau[i]==2:
            compteur2=compteur2+1
        i=i+1

    if compteur1>compteur2 :
        return '1'

    elif compteur2>compteur1:
        return '2'

    elif compteur1==compteur2:
        return '0'




"""partie 3"""
from os import system
import os
import json


def creer_partie(n):
    return {"plateau":creer_plateau(n), "joueur":1}


def saisie_valide(partie, s):
    if s == "M" or (len(s) == 2 and case_valide(partie["plateau"], ord(s[0])-97, int(s[1])-1)):
        return True
    else:
        return False


def tour_jeu(partie):
    system('clear') 
    afficher_plateau(partie["plateau"])
    if joueur_peut_jouer(partie["plateau"], partie["joueur"]):
        print("joueur", partie["joueur"],"a vous de jouer")
        choix = input()
        good_input = False
        while not good_input:
            if not saisie_valide(partie, choix):
                print("La saisie n'est pas valide, réesayez:")
                choix = input()
            elif choix != "M" and not mouvement_valide(partie["plateau"], ord(choix[0])-97, int(choix[1])-1, partie["joueur"]):
                print("Le mouvement n'est pas possible, réesayez:")
                choix = input()
            else:
                good_input = True
        if choix != "M":
            mouvement(partie["plateau"], ord(choix[0])-97, int(choix[1])-1, partie["joueur"])
            return True
        return False  
    return True      


def saisir_action(partie):
    print("Choisissez une action:")
    print("0 pour terminer le jeu")
    print("1 pour commencer une nouvelle partie")
    print("2 pour charger une partie")
    print("3 pour sauvegarder une partie (si une partie est en cours)")
    print("4 pour reprendre la partie (si une partie est en cours)")
    choix = input()
    if partie is None:
        while choix != "0" and choix != "1" and choix != "2":
            if choix == "3" or choix == "4":
                print("Pas de partie en cours, choisissez une autre action:")
            else:
                print("Saisie invalide, réesayez:")
            choix = input()
    else:
        while choix != "0" and choix != "1" and choix != "2" and choix != "3" and choix!= "4":
            print("Saisie invalide, réesayez:")
            choix = input()
    return choix        


def jouer(partie):
    while not fin_de_partie(partie["plateau"]):
        if tour_jeu(partie):
            partie["joueur"] = pion_adverse(partie["joueur"])
        else:
            return False
    system('clear')      
    win = gagnant(partie["plateau"])
    afficher_plateau(partie["plateau"])
    print("La partie est terminée !")
    if win == 0:
        print("égalité.")
    else:
        print("Le joueur ",win," à gagné.")
    return True


def saisir_taille_plateau():
    print("saisir (4, 6 ou 8).")
    choix = int(input())
    while choix != 4 and choix != 6 and choix != 8:
        print("invalide, réesayez:")
        choix = int(input())
    return choix   


def sauvegarder_partie(partie):
    with open("sauvegarde_partie.json", "w") as save:
        json.dump(partie, save)


def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        with open("sauvegarde_partie.json", "r") as save:
            return json.load(save)
    else:
        print("Il n'y a pas de partie sauvegardée")
        return creer_partie(saisir_taille_plateau())        

def othello():
    partie = None
    action = saisir_action(partie)
    while action != "0":
        if action == "1":
            partie = creer_partie(saisir_taille_plateau())
            jouer(partie)
        elif action == "2":
            partie = charger_partie()
            jouer(partie)
        elif action == "3":
            sauvegarder_partie(partie)
        else:
            jouer(partie)
        action = saisir_action(partie)
    system('clear') 
    
othello()         