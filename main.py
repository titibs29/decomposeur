from ctypes.wintypes import HENHMETAFILE


# composition d'une courbe sur base de sa serie de fourier

# auteurs:
#     Thibaut Rizzoli (thibaut.rizzoli@hotmail.be)

# entreprise:
#     HEH (www.heh.be)

# imports et pré exec
import matplotlib.pyplot as plt
import csv


def compose(harmoniques = "input.csv",fonction = "output.csv"):
    # lecture des entrees
    # nous devons ouvrir le fichier CSV comprenant les amplitudes ainsi que les fréquences 
    # format: f(t)=a0+a1*cos(wt)+b1*sin(wt)+...+an*cos(nwt)+bn*sin(nwt)+...
    # a noter que les fonction paires gardent uniquement la composante cos, et vice versa
    with open(harmoniques, 'R', newline=' ') as csvInFile:
        serieDeFourier = csv.reader(csvInFile, delimiter= ' ', quotechar='|')
        
    # algo

    print (serieDeFourier)

    courbe = {'time':'voici le point en x', 'amp': 'voici le point en y'}

    # affichage du graphique (matplotlib)


    # ecriture sur un fichier de sortie
    with open(fonction, 'W', newline = ' ') as csvOutFile:
        ecrivain = csv.writer(csvOutFile, delimiter=' ', quotechar= '|', quoting=csv.QUOTE_MINIMAL)
        ecrivain.writerow('debut')
        for row in courbe:
            ecrivain.writerow(courbe[row])



if __name__ == "__main__":
    # boucle si lecture seule
    print("lecture du fichier input.csv")
    compose("input.csv","output.csv")