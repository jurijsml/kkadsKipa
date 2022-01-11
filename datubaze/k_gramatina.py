#Kontaktu grāmatiņa

import d_gramatina

def kontaktu_piev():
  vards = input("Lūdzu, ievadiet kontakta vārdu: ")
  numurs = input("Lūdzu, ievadiet kontakta numuru: ")

  print(f"Pievieno {vards} ar numuru - {numurs}")

  d_gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()

#Kontaktu atrašana. (Meklē pēc pilnā vārda)
def kont_atrasana():
  vards = input("Lūzu, ievadi kontakta vārdu, kuru meklē: ")
  numurs = d_gramatina.atrod_kontaktu(vards)

  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    print(f"Izskatās, ka {vards} nav sarakstā")

kont_atrasana()

def galvena_izv():
  print(sakums)
  izvele = input("Tava izvēlētā darbība: ")

  if izvele == "1":
    kontaktu_piev()
  elif izvele == "2":
    kont_atrasana()
  else:
    print("Neeksistējoša darbība, lūdzu, mēģini vēlreiz!")

while True:
  galvena_izv()
  input("\nNospied Enter, lai turpinātu\n\n")
  