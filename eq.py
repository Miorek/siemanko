import random
def gra():
    eq = {"miecz":1,"mikstura": 3,"zloto":30}
    wagaeq = {"miecz": 5, "mikstura": 1, "zloto": 0}
    wartosceq = {"miecz": 10, "mikstura": 2, "zloto": 1}
    udzwig = 100
    true = True
    while True:
        print("----MENU-------")
        print("1 - wyswietl ekwipunek")
        print("2 - stworz nowy przedmiot")
        print("3 - uzyj przedmiotu")
        print("4 - sprawdz przedmiot")
        print("5 - skelp")
        print("6 - sprzedaj przedmiot")
        print("7 - wyjdz")
        x = int(input("wybierz opcje:"))
        if x == 7:
            break
        elif x == 6:
            sprzedaj(eq,wartosceq)
        elif x == 2:
            stworz_item(eq, wartosceq, wagaeq)
        elif x == 5:
            sklep(eq, wartosceq, wagaeq, udzwig)
        elif x == 4:
            sprawdz_item(eq, wartosceq, wagaeq)
        elif x == 3:
            uzyj_item(eq)
    #    elif x == 2:
    #        dodaj_item()
        elif x == 1:
            wyswietl_eq(eq, wagaeq)



def wyswietl_eq(eq, wagaeq):
    print("EKWIPUNEK")
    for item, ilosc in eq.items():
        print(item, ":", ilosc)
    waga = sum(wagaeq[item] * ilosc for item, ilosc in eq.items())
    print(waga, "z 100 udzwigu")

#def dodaj_item():
#    z = input("Jaki przedmiot chcesz dodac: ").strip().lower().replace(" ", "")
#   if z not in eq:
#        print("nie posiadasz takiego przedmiotu")
#        return
#    maxeq=sum(wagaeq[item] * ilosc for item, ilosc in eq.items())

#   if maxeq + wagaeq[z]> udzwig:
#        print("masz pelny ekwipunek")
#    else:
#        eq[z] += 1 
#        print("Dodano przedmiot")
def uzyj_item(eq):
    a = input("jakiego przedmiotu chcesz uzyc     ").strip().lower().replace(" ", "")
    eq[a] -= 1
    if eq[a]==0:
        del eq[a]
        print("niemasz juz wiecej tego przedmiotu")
    else:
        print("zmniejszono ilosc przedmiotu")
def sprawdz_item(eq, wagaeq, wartosceq):
    y = input("jaki przedmiot chcesz sprawdzic      ").strip().lower().replace(" ", "")
    if y in eq:
        print("ilosc:", eq[y])
        print("waga:", wagaeq[y])
        print("wartosc:", wartosceq[y])
    else:
        print("niemasz takiego przedmiotu")
def stworz_item(wagaeq, wartosceq, eq):
    g = input("jaki przedmiot chcesz dodac ").strip().lower().replace(" ", "")
    if g in eq:
        print("taki przedmiot juz istnieje:")
        return
    wagaeq[g] = random.randint(1,10)
    wartosceq[g] = random.randint(1,10)
    eq[g] = 0 

    print("stworzono przedmiot: ", g)
    print("waga:", wagaeq[g])
    print("wartosc", wartosceq[g])

def sklep(eq,wartosceq, wagaeq, udzwig):
    print("-----SKLEP------")
    for item in wartosceq:
        if item != "zloto":
            print(item, " Cena:", wartosceq[item], "zlota",
                  " Waga:", wagaeq[item])
    kup = input("co chcesz kupic: ").strip().lower().replace(" ", "")
    if kup not in wartosceq or kup == "zloto":
        print("Nie ma takiego przedmiotu w sklepie")
        return
    cena = wartosceq[kup]
    if eq.get("zloto", 0) < cena:
        print("nie masz wystarczajaco zlota")
        return
    waga = sum(wagaeq[item] * ilosc for item, ilosc in eq.items())
    if waga + wagaeq[kup] > udzwig:
        print("nie masz miejsca w ekwipunku")
        return
    eq["zloto"] -= cena
    eq[kup] = eq.get(kup, 0) + 1
    print("Kupiono:", kup)
def sprzedaj(eq, wartosceq):
    print("----SPRZEDAZ----")
    for item, ilosc in eq.items():
        if item != "zloto" and ilosc > 0:
            print(item, "| Ilosc:", ilosc,
                  "| Cena:", wartosceq[item], "zlota")
    sprz = input("Co chcesz sprzedac: ").strip().lower().replace(" ", "")
    if sprz not in eq or sprz == "zloto" or eq[sprz] <= 0:
        print("Nie masz takiego przedmiotu")
        return
    cena = wartosceq[sprz]
    eq[sprz] -= 1
    eq["zloto"] = eq.get("zloto", 0) + cena
    if eq[sprz] == 0:
        del eq[sprz]
    print("Sprzedano:", sprz)
    print("Otrzymano:", cena, "zlota")

gra()

    