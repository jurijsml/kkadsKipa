#Kontaktu grāmatiņa

import d_gramatina

def kontaktu_piev():
  vards = input("Lūdzu, ievadiet kontakta vārdu: ")
  numurs = input("Lūdzu, ievadiet kontakta numuru: ")

  print(f"Pievieno {vards} ar numuru - {numurs}")

  d_gramatina.piev_kontaktu(vards, numurs)

#kontaktu_piev()

#Kontaktu atrašana. (Meklē pēc pilnā vārda)
def kont_atrasana():
  vards = input("Lūzu, ievadi kontakta vārdu, kuru meklē: ")
  numurs = d_gramatina.atrod_kontaktu(vards)

  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit = d_gramatina.kont_meklesana(vards)
    if sakrit:
      for k in sakrit:
       print(f"{k} numurs ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {vards} nav sarakstā")

#Kontaktu rediģēšana
def kontaktu_red():
  iepr_v = input("Ievadi kontakta vārdu, kuru vēlies rediģēt: ")
  iepr_numurs = d_gramatina.atrod_kontaktu()

  if iepr_numurs:
    jaunais_v = input(f"Ievadi {iepr_v} kontakta jauno vārdu (ja nevēlies mainīt vārdu, atstāj tukšu): ")
    jaunais_n = input(f"Ievadi {iepr_numurs} kontakta jauno numuru (ja nevēlies mainīt numuru, atstāj tukšu): ")

    if not jaunais_v:
      d_gramatina.mainit_numuru(iepr_v, jaunais_n)

    if not jaunais_n:
      jaunais_n = iepr_numurs

    else:
      d_gramatina.mainit_kontaktu(iepr_v, jaunais_v, jaunais_n)
  


def galvena_izv():
  sakums = ("\n1 - Kontaktu pievienošana\n2 - Kontakta meklēšana\n")
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
  input("\nNospied Enter, lai turpinātu\n")