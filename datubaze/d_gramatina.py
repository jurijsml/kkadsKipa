from replit import db #Datu bāzes pievienošana

#Funkcija, kura pievieno jaunus kontaktus
def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print("Kontakts jau ir pievienots.")
  else:
    db[vards]=tel_nr
    print(f"Pievienots: {vards}:{tel_nr}.")

#Meklēšanas funkcija. (Meklē pēc pilna vārda jeb atslēgas)
def atrod_kontaktu(vards):
  numurs = db.get(vards)
  return numurs

#Meklēšanas funkcija (meklē pēc simbola)
def kont_meklesana(simbols):
    meklet = db.prefix(simbols)
    return {k: db[k] for k in meklet}


#Rediģēšana
#Mainām numuru
def mainit_numuru(iepr_v, jaunais_n):
  db[iepr_v]=jaunais_n
  print(f"Kontakta {iepr_v} jaunais numurs ir {jaunais_n}.")
#Mainām visu kontaktu
def mainit_kontaktu(iepr_v, jaunais_v, jaunais_n):
  db[jaunais_v] = jaunais_n
  del db[iepr_v]
  print (f"Jaunais vārds ir {jaunais_v} un jaunais numurs ir {jaunais_n}.")

#Kontakta dzēšana
def dzest_kont(vards):
  del db[vards]
  print(f"Kontakts {vards} ir izdzēsts.")