#Kontaktu grāmatiņa

import d_gramatina

def kontaktu_piev():
  vards = input("Lūdzu, ievadiet kontakta vārdu: ")
  numurs = input("Lūdzu, ievadiet kontakta numuru: ")

  print(f"Pievieno {vards} ar numuru - {numurs}")

  d_gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()

def kont_atrasana():
  vards = input("Lūzu, ievadi kontakta vārdu, kuru meklē: ")
  numurs = d_gramatina.atrod_kontaktu(vards)

  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    print(f"Izskatās, ka {vards} nav sarakstā")

kont_atrasana()