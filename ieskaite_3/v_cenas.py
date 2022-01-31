import d_cenas

def precu_piev():
  nosauk = input("Lūdzu, ievadiet preces nosaukumu: ")
  cena = input("Lūdzu, ievadiet preces cenu: ")
  masa = input("Lūdzu, ievadiet preces masu (gramos): ")

  print(f"Pievieno {nosauk} ar cenu - {cena} un masu {masa}")

  d_cenas.piev_preci(nosauk, cena, masa)

def precu_atrasana():
  nosauk = input("Lūzu, ievadi preces nosaukumu, kuru meklē: ")
  cena = d_cenas.atrod_preci(nosauk)
  masa = d_cenas.atrod_preci(nosauk)

  if cena:
    print(f"{nosauk} cena ir €{cena}, un masa - {masa}g")
  else:
    sakrit = d_cenas.precu_meklesana(nosauk)
    if sakrit:
      for k in sakrit:
       print(f"{k} cena ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {nosauk} nav sarakstā")

def precu_red():
  iepr_n = input("Ievadi preces nosaukumu, kuru vēlies rediģēt: ")
  iepr_cena = d_cenas.atrod_preci(iepr_n)
  
  if iepr_cena:
    jaunais_n = input(f"Ievadi preces ({iepr_n}) jauno nosaukumu (ja nevēlies mainīt nosaukumu, atstāj tukšu): ")
    jauna_c = input(f"Ievadi preces ({iepr_cena}) jauno cenu (ja nevēlies mainīt cenu, atstāj tukšu): ")

    if not jaunais_n:
      d_cenas.mainit_cenu(iepr_n, jauna_c)

    if not jauna_c:
      jauna_c = iepr_cena

    else:
      d_cenas.mainit_preci(iepr_n, jaunais_n, jauna_c)
  else:
    print(f"Izskatās, ka {iepr_n} nav sarakstā.")

def precu_dzesana():
  nosauk = input("Ievadi preces nosaukumu, kuru vēlies dzēst: ")
  cena = d_cenas.atrod_preci(nosauk)

  if cena:
    lemums = input(f"Vai jūs tiešām vēlaties izdzēst šo preci: {nosauk} - {cena}? (1 - Jā, 2 - Nē)")

    if lemums == "1":
      d_cenas.dzest_preci(nosauk)
    else:
      print(f"Prece {nosauk} netika dzēsta.")
  else:
   print("Neeksistējoša darbība, lūdzu, mēģini vēlreiz!")

def galvena_izv():
  sakums = ("\n1 - Preču pievienošana\n2 - Preces meklēšana\n3 - Preces rediģēšana\n4 - Preces dzēšana\n5 - Iziet")
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