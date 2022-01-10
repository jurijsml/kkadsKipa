from replit import db


def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print("Kontakts jau ir pievienots")
  else:
    db[vards]=tel_nr
    print(f"Pievienots: {vards}:{tel_nr}")

def atrod_kontaktu(vards):
  numurs = db.get(vards)
  return numurs