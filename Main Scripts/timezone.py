def zaman(veri,adim):
    QRSOrTime = []
    sayici = 0.
    for row in veri:
        if row != 0:
            sayici = sayici + adim
    QRSOrTime.append(float(sayici))

    return QRSOrTime