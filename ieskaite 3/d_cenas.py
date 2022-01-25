from replit import db #Datu bāzes pievienošana

#Funkcija, kura pievieno jaunus kontaktus
def piev_preci(nosauk, cena):
  if nosauk in db:
    print("Prece jau ir pievienota.")
  else:
    db[nosak]=cena
    print(f"Pievienots: {nosauk}:{cena}.")

#Meklēšanas funkcija. (Meklē pēc pilna vārda jeb atslēgas)
def atrod_preci(nosauk):
  cena = db.get(nosauk)
  return cena

#Meklēšanas funkcija (meklē pēc simbola)
def precu_meklesana(simbols):
    meklet = db.prefix(simbols)
    return {k: db[k] for k in meklet}


#Rediģēšana
#Mainām numuru
def mainit_cenu(iepr_n, jaunais_n):
  db[iepr_n]=jauna_c
  print(f"Kontakta {iepr_v} jaunais numurs ir {jaunais_n}.")
#Mainām visu kontaktu
def mainit_preci(iepr_n, jaunais_n, jauna_c):
  db[jaunais_n] = jauna_c
  del db[iepr_n]
  print (f"Jaunais vārds ir {jaunais_n} un jaunais numurs ir {jauna_c}.")

#Kontakta dzēšana
def dzest_preci(nosauk):
  del db[nosauk]
  print(f"Kontakts {nosauk} ir izdzēsts.")