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
  