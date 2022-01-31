from replit import db

def piev_preci(nosauk, cena, masa):
  if nosauk in db:
    print("Prece jau ir pievienota.")
  else:
    db[nosauk]=cena
    print(f"Pievienots: {nosauk}:€{cena}:{masa}g.")

def atrod_preci(nosauk):
  cena = db.get(nosauk)
  return cena

def precu_meklesana(simbols):
    meklet = db.prefix(simbols)
    return {k: db[k] for k in meklet}

def mainit_cenu(iepr_n, jauna_c, jauna_m):
  db[iepr_n]=jauna_c
  print(f"Kontakta {iepr_n} jaunā cena ir €{jauna_c}.")

def mainit_masu(iepr_masa, jauna_m, jaunais_n, iepr_n):
  db[iepr_n]=jauna_m
  print(f"Preces {iepr_n} jaunā masa ir {jauna_m}g.")

def mainit_preci(iepr_n, jaunais_n, jauna_c, jauna_m):
  db[jaunais_n] = jauna_c
  del db[iepr_n]
  print (f"Jaunais nosaukums ir {jaunais_n} un jaunā cena ir {jauna_c}.")

def dzest_preci(nosauk):
  del db[nosauk]
  print(f"Prece {nosauk} ir izdzēsta.")