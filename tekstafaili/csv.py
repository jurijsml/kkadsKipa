import csv

fails=open("csv_meg.csv")

lasit_csv=csv.reader(fails)
print(lasit_csv)

header=[]
header=next(lasit_csv)

print(header)

saturs=[]
for rinda in lasit_csv:
  saturs.append(rinda)
print(saturs)

fails.close()


kolonnunosaukumi=['Vārds','1.atzime','2.atzime']
dati=[['Anna',9,8],['Viesturis',6,5],['Kārlis',9,10],['Sibilla',9,5]]
with open('skolenu_atzimes.cvs','w') as f:
  csvwriter=csv.writer(f)
  csvwriter.writerow(kolonnunosaukumi)
  csvwriter.writerows(dati)