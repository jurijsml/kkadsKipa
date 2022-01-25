 #Kontaktu grāmatiņa

import d_cenas

def precu_piev():
  nosauk = input("Lūdzu, ievadiet kontakta vārdu: ")
  cena = input("Lūdzu, ievadiet kontakta numuru: ")

  print(f"Pievieno {nosauk} ar numuru - {cena}")

  d_cenas.piev_precu(nosauk, cena)

#Kontaktu atrašana. (Meklē pēc pilnā vārda)
def precu_atrasana():
  nosauk = input("Lūzu, ievadi kontakta vārdu, kuru meklē: ")
  cena = d_cenas.atrod_preci(nosauk)

  if cena:
    print(f"{nosauk} numurs ir {cena}")
  else:
    sakrit = d_cenas.precu_meklesana(nosauk)
    if sakrit:
      for k in sakrit:
       print(f"{k} numurs ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {nosauk} nav sarakstā")

#Kontaktu rediģēšana
def precu_red():
  iepr_m = input("Ievadi kontakta vārdu, kuru vēlies rediģēt: ")
  iepr_cena = d_cenas.atrod_preci(iepr_n)

  if iepr_cena:
    jaunais_n = input(f"Ievadi {iepr_n} kontakta jauno vārdu (ja nevēlies mainīt vārdu, atstāj tukšu): ")
    jauna_c = input(f"Ievadi {iepr_c} kontakta jauno numuru (ja nevēlies mainīt numuru, atstāj tukšu): ")

    if not jaunais_n:
          d_cenas.mainit_cenu(iepr_n, jauna_c)

    if not jauna_c:
      jauna_c = iepr_c

    else:
      d_cenas.mainit_preci(iepr_n, jaunais_n, jauna_c)
  else:
    print(f"Izskatās, ka {iepr_n} nav sarakstā.")
  
#Kontaktu dzēšana

def precu_dzesana():
  nosauk = input("Ievadi kontakta vārdu, kuru vēlies dzēst: ")
  cena = d_cenas.atrod_preci(nosauk)

  if cena:
    lemums = input(f"Vai jūs tiešām vēlaties izdzēst šo kontaktu: {nosauk} - {cena}? (1 - Jā, 2 - Nē)")

    if lemums == "1":
      d_cenas.dzest_preci(nosauk)
    else:
      print(f"Kontakts {nosauk} netika dzēsts.")
  else:
   print("Neeksistējoša darbība, lūdzu, mēģini vēlreiz!")

def galvena_izv():
  sakums = ("\n1 - Kontaktu pievienošana\n2 - Kontakta meklēšana\n3 - Kontakta rediģēšana\n4 - Kontakta dzēšana\n5 - Iziet")
  print(sakums)
  izvele = input("Tava izvēlētā darbība: ")
  
  if izvele == "1":
    precu_piev()
  elif izvele == "2":
    precu_atrasana()
  elif izvele == "3":
    precu_red()
  elif izvele == "4":
    precu_dzesana()
while True:
  galvena_izv()
  input("\nNospied Enter, lai turpinātu!\n")