import sqlite3

db = sqlite3.connect('test.db')

#Tabulas izveide
db.execute("""
           CREATE TABLE IF NOT EXISTS darbinieki
           (id      INTEGER   PRIMARY KEY    NOT NULL,
           vards     TEXT     NOT NULL,
           alga      REAL,
           piezimes  CHAR(50)
           )
           """)

#Datu pievienošana
# db.execute("""INSERT INTO darbinieki
#            (id,vards,alga,piezimes)
#            VALUES(3,'Zane',700,'E-komercija')
#            """)

#db.commit()

#Datu iegūšana
dati = db.execute("""SELECT * FROM darbinieki
                  WHERE id=1
                  """)
rezultats = dati.fetchall()
print(rezultats)

#Tabulas izveide, izmantojot automātisko id ģenerēšanu
db.execute(
  """
  CREATE TABLE IF NOT EXISTS premijas
  (id   INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
  pceturksnis   REAL,
  oceturksnis   REAL,
  tceturksnis   REAL,
  cceturksnis   REAL
  )
  """
)


# p_ceturksnis = input("Ievadiet pirmā ceturkšņa prēmiju: ")
# o_ceturksnis = input("Ievadiet otrā ceturkšņa prēmiju: ")
# t_ceturksnis = input("Ievadiet trešā ceturkšņa prēmiju: ")
# c_ceturksnis = input("Ievadiet ceturtā ceturkšņa prēmiju: ")

# db.execute("""
#            INSERT INTO premijas
#            (pceturksnis,oceturksnis,tceturksnis,cceturksnis)
#            VALUES(:pceturksnis,:oceturksnis,:tceturksnis,:cceturksnis)
#            """,{'pceturksnis':p_ceturksnis,'oceturksnis':o_ceturksnis,'tceturksnis':t_ceturksnis,'cceturksnis':c_ceturksnis})

# db.commit()

dati = db.execute("""SELECT * FROM premijas
                  WHERE id=1
                  """)
rezultats = dati.fetchall()
print(rezultats)

dati = db.execute("""SELECT * FROM darbinieki
                  JOIN premijas
                  ON darbinieki.id = premijas.id
                  """)
rezultats = dati.fetchall()
print(rezultats)

for rinda in rezultats:
  print("ID:",rinda[0])
  print("Vārds:",rinda[1])
  print("Alga:",rinda[2])
  print("Komentārs:",rinda[3])
  print("Prēmijas:")
  print("Pirmā ceturkšņa prēmija:",rinda[5])
  print("Otrā ceturkšņa prēmija:",rinda[6])
  print("Trešā ceturkšņa prēmija:",rinda[7])
  print("Ceturtā ceturkšņa prēmija:",rinda[8])
  print("\n")