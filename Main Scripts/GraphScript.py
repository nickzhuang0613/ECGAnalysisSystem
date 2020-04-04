import matplotlib.pyplot as plt
import scipy.signal as scs
import csv
from QRS import qrs
import PT as pt
from OtherWindow import details as Details

def GraphScript(dosyadi,zaman):

    hamveri = []

    time = int(zaman)     # SİNYAL SÜRESİ
    a = 0

    with open(dosyadi,'r') as txtfile:            # SİNYAL OKUMA
        txtfile = csv.reader(txtfile)
        for row in txtfile:
            hamveri.append(float(row[1]))

    veriuzunlugu = len(hamveri)                       # HAM SİNYAL UZUNLUĞU
    Fs = veriuzunlugu // time                        # ÖRNEKLEM FREKANSI
    Ts = 1 / Fs

    periyod = []
    per = 0

    for row in range(len(hamveri)):
        per = per + Ts
        periyod.append(per)

    [b, c] = scs.butter(1, 10/(Fs/2), btype='highpass',analog=False)   # Filtreleme
    filtresinyal = scs.filtfilt(b, c, hamveri)

    sayacQRS = 0                                      # QRS DÖNGÜSÜ İÇİN SAYAÇ
    geciciQRS = []                                    # GEÇİCİ QRS LİSTESİ
    QRS = []                                          # SEÇİLMİŞ QRS LİSTESİ
    for row in range(veriuzunlugu):
        sayacQRS += 1
        geciciQRS.append(float(filtresinyal[row]))
        if sayacQRS == veriuzunlugu:
            QRS = qrs(geciciQRS,Fs)

    gercekQRS =[]
    for row in range(len(QRS[0])):
        gercekQRS.append(QRS[0][row])

    sayacPT = 0
    PT = []
    for row in range(veriuzunlugu):
        sayacPT += 1
        if sayacPT == veriuzunlugu:
            PT.append(pt.PT(hamveri,gercekQRS,Fs))


    plt.subplot(3,1,1)
    plt.plot(periyod,hamveri)
    plt.ylabel("Genlik")
    plt.xlabel("Zaman(sn)")
    plt.title("Hamveri")
    plt.subplots_adjust(hspace=1)
    plt.subplot(3,1,2)
    plt.plot(periyod,filtresinyal)
    plt.ylabel("Genlik")
    plt.xlabel("Zaman(sn)")
    plt.title("Filtre Sinyal")
    plt.subplots_adjust(hspace=1)
    plt.subplot(3,1,3)
    plt.plot(gercekQRS)
    plt.xlabel("Örnek Sayısı")
    plt.ylabel("Genlik")
    plt.title("QRS Kompleksleri")
    plt.subplots_adjust(hspace=1)
    plt.show()


