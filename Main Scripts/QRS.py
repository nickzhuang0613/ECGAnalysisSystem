import math
import statistics as sts
def qrs(veri,Fs):

    QRS = []
    geciciQRS = []
    sayac = 0
    toplamDongu = 0
    gercekFs = Fs//2
    Roncesi = 5*Fs/100
    RListe = []

    for row in range(len(veri)):
        sayac += 1
        geciciQRS.append(veri[row])
        if sayac % gercekFs == 0:

            R = max(geciciQRS)
            RListe.append(R)
            Rindex = geciciQRS.index(R)
            S = min(geciciQRS)
            Sindex = geciciQRS.index(S)

            print("{0}. Fs katı Rindex : {1} ve Sindex : {2} ".format(sayac,Rindex,Sindex))

            for raw in range(toplamDongu,sayac):
                if raw <= Rindex-Roncesi:
                    QRS.append(0)
                elif raw > Rindex-Roncesi and raw <= Sindex+Roncesi:
                   QRS.append(geciciQRS[raw]*2)
                else:
                    QRS.append(0)

            for i in range(len(geciciQRS)):
                geciciQRS[i] = 0
            toplamDongu = toplamDongu + gercekFs

    toplam = 0
    avg = 0
    toplamvar = 0
    standart = 0
    newRList = []
    for raw in RListe:
        toplam = toplam + raw
    avg = toplam / len(RListe)
    for rew in RListe:
        toplamvar = toplamvar + (avg-rew)**2
    standart = toplamvar / len(RListe)
    standart = math.sqrt(standart)
    for r in range(len(RListe)):
        if RListe[r] >= standart*2:
            newRList.append(RListe[r])
    sortedQRS = sorted(QRS)
    medi = sts.median(sortedQRS)
    newQRS = []
    for i in range(len(QRS)):
        if math.fabs(QRS[i]) >= standart*0.8 or QRS[i] == 0:
            newQRS.append(QRS[i])

    return newQRS,newRList