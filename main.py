from signals import convToFourier

#signal � convertir (�cart de temps: 1)
signal =[5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,5,5,5,5,5,-5,-5,-5,-5,-5,]



if __name__ == "__main__":
    # boucle principale
    fourier = []
    fourier = convToFourier(signal)
    print(fourier)