import csv

veri = []

with open('./Csv Test Data/45,2.csv','r') as csvfile:
    csvfile = csv.reader(csvfile,delimiter=',')
    for row in csvfile:
        veri.append(float(row[1]))
print(veri)

with open('./Txt Test Data/45,2.txt','w') as txtfile:
    filewriter = csv.writer(txtfile)
    filewriter.writerow(map(lambda x: x, veri))

