#w- writing jeb rakstišanas stāvoklis
#r-lasisana
#a-teksta beigās piev.

fails=open('pirmais.txt',"w",encoding="utf-8")

fails.write("Sveiki!")

saturs=["Ir 2022 gads\n","Ārā snieg\n"]

fails.writelines(saturs)

fails.close()

with open('pirmais.txt',"r",encoding="utf-8") as f:
  print(f.read())
  print(f.readline())



with open('pirmais.txt',"a",encoding="utf-8") as f:
 f.write("Es esmu te")