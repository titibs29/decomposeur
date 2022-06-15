from signals import convToFourier

#signal à convertir (écart de temps: 1)
signal =[5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,]



if __name__ == "__main__":
    # boucle principale
    fourier = []
    fourier = convToFourier(signal)
    print(fourier)