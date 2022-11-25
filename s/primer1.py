import random
# brojpokusaja =  7
# poeni = 0

# while brojpokusaja > 0:
#     srecanbroj = random.randint(1, 20)
#     mojbroj = int(input("unesi broj:"))

#     if srecanbroj == mojbroj:
#         print("pogodak", mojbroj, "srecan broj:", srecanbroj)
#     else:
#         print("promasaj", mojbroj, "srecan broj:", srecanbroj)

# for broj in range (1,10):
#     print(broj)
#     if broj == 5:
#         break
    

# for broj in range (1,10):
#     if broj == 3:
#        continue
# #     print(broj)       # preskace broj 3, drugi nacin

# for ime in ["petar", "","marko" ,"katarina"]:
#     if ime == "jovana":
#         print("pronadjena!")
#         break
#     print(ime)
# else:
#     print("zavrseno citanje")

zbir = 0
while True:
    broj = input("unesite broj:")

    if broj == "":
        print("zbir je", zbir)
    elif broj.isnumeric():
        zbir +=int(broj)
    elif broj == "quit":
        break
    else:
        print("proverite unos")

print("caooooo!!!!!!!!!!")
  