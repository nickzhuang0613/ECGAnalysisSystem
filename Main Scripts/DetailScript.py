import matplotlib.pyplot as plt
import scipy.signal as scs
import csv
from QRS import qrs
from OtherWindow import details as Details
from timezone import zaman as sure

def DetailScript(dosyadi,zaman):

    hamveri = []

    time = int(zaman)     # SİNYAL SÜRESİ
    a = 0

    with open(dosyadi,'r') as txtfile:            # SİNYAL OKUMA
        txtfile = csv.reader(txtfile)
        for row in txtfile:
            hamveri.append(float(row[1]))

    veriuzunlugu = len(hamveri)                       # HAM SİNYAL UZUNLUĞU
    Fs = veriuzunlugu // time                        # ÖRNEKLEM FREKANSI

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

    RListe = []
    for row in range(len(QRS[1])):
        RListe.append(QRS[1][row])

    QRSsayisi = len(RListe)
    PTsayisi = QRSsayisi
    adim = 1/Fs
    counter = 0
    qrstime = []
    gecici = []
    for i in range(len(gercekQRS)):
        counter += 1
        gecici.append(gercekQRS[i])
        if counter % (Fs // 2 ) ==0:
            qrstime.append(sure(gecici,adim))
            print(len(gecici))
            gecici = []
    totaltime = 0
    timecount = 0
    for raw in range(len(qrstime)):
        if qrstime[raw][0] != 0.0 and qrstime[raw][0] >= 0.05:
            print(qrstime[raw][0])
            timecount += 1
            totaltime = totaltime + qrstime[raw][0]

    qrszamani = totaltime/timecount

    Details(qrscount=QRSsayisi,ptcount=PTsayisi,qrstime=qrszamani,hamveri=hamveri,Fs=Fs)
