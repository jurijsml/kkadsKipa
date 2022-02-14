from replit import db

def piev_preci(nosauk, cena):
  if nosauk in db:
    print("Prece jau ir pievienota.")
  else:
    db[nosauk]=cena
    print(f"Pievienots: {nosauk}:€{cena}.")

def atrod_preci(nosauk):
  cena = db.get(nosauk)
  return cena

def precu_meklesana(simbols):
    meklet = db.prefix(simbols)
    return {k: db[k] for k in meklet}

def mainit_cenu(iepr_n, jauna_c):
  db[iepr_n]=jauna_c
  print(f"Kontakta {iepr_n} jaunā cena ir €{jauna_c}.")

def mainit_preci(iepr_n, jaunais_n, jauna_c):
  db[jaunais_n] = jauna_c
  del db[iepr_n]
  print (f"Jaunais nosaukums ir {jaunais_n} un jaunā cena ir {jauna_c}.")

def dzest_preci(nosauk):
  del db[nosauk]
  print(f"Prece {nosauk} ir izdzēsta.")