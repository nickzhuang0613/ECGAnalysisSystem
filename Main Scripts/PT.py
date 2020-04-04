def PT(hamveri,QRS,Fs):

    PTListe = []

    for row in range(len(QRS)):

        if QRS[row] == 0:
            PTListe.append(hamveri[row])

        elif QRS[row] != 0:
            PTListe.append(hamveri[0])
    return PTListe




