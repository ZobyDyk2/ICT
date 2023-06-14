import random

def zahraj_hru():
    print("Vítejte ve hře 'Záchrana princezny'!")
    print("Princezna je unesena zlým drakem.")
    print("Vaším úkolem je projít několika místnostmi a zachránit princeznu.")
    print("Vyberte si jednu z místností: ")
    print("1. Temný les")
    print("2. Horská jeskyně")
    print("3. Starý hrad")
    print("4. Magický pramen")

    mistnost = int(input("Zadejte číslo místnosti: "))
    hraj(mistnost)

def hraj(mistnost):
    if mistnost == 1:
        print("\nJste ve temném lese.")
        print("Vidíte před sebou tři cesty.")
        print("Kterou cestou se chcete vydat?")
        print("1. Cesta vpravo")
        print("2. Cesta vlevo")
        print("3. Stezka rovně")

        cesta = int(input("Zadejte číslo cesty: "))
        if cesta == 1:
            print("\nNacházíte se u hlubokého propasti.")
            print("Nemůžete ji překonat a vracíte se zpět.")
            hraj(1)
        elif cesta == 2:
            print("\nDostáváte se na mýtinu.")
            print("Najednou se před vámi objevuje drak!")
            boj_s_drakem()
        elif cesta == 3:
            print("\nJdete po stezce rovně až k řece.")
            print("Nemůžete přejít řeku a vracíte se zpět.")
            hraj(1)
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            hraj(1)

    elif mistnost == 2:
        print("\nJste v horské jeskyni.")
        print("Vidíte před sebou dvě cesty.")
        print("Kterou cestou se chcete vydat?")
        print("1. Rozcestí vpravo")
        print("2. Rozcestí vlevo")

        cesta = int(input("Zadejte číslo cesty: "))
        if cesta == 1:
            print("\nDostáváte se do temného tunelu.")
            print("Bohužel se v něm ztrácíte a vracíte se zpět.")
            hraj(2)
        elif cesta == 2:
            print("\nDostáváte se ke skrytému pokladu.")
            print("Z pokladu vytahujete meč a zachraňujete princeznu.")
            vyhra()
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            hraj(2)

    elif mistnost == 3:
        print("\nJste ve starém hradě.")
        print("Vidíte před sebou uzamčené dveře.")
        print("Jakým způsobem se je pokusíte otevřít?")
        print("1. Použijete klíč")
        print("2. Rozkopnete dveře")

        cesta = int(input("Zadejte číslo způsobu: "))
        if cesta == 1:
            print("\nNesprávný klíč. Dveře se neotvírají.")
            hraj(3)
        elif cesta == 2:
            print("\nRozkopáváte dveře a dostáváte se do věže.")
            print("Nahoře ve věži nacházíte princeznu.")
            vyhra()
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            hraj(3)

    elif mistnost == 4:
        print("\nJste u magického pramene.")
        print("Pramen vydává zářivé světlo.")
        print("Co uděláte?")
        print("1. Napít se z pramene")
        print("2. Prohlédnout si pramen")

        cesta = int(input("Zadejte číslo akce: "))
        if cesta == 1:
            print("\nKdyž se napijete z pramene, objevíte skrytou cestu.")
            print("Procházíte cestou a zachraňujete princeznu.")
            vyhra()
        elif cesta == 2:
            print("\nKdyž si prohlížíte pramen, ztrácíte čas.")
            print("Najednou se objevuje drak a unáší princeznu.")
            boj_s_drakem()
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            hraj(4)

    else:
        print("Neplatný vstup. Zkuste to znovu.")
        zahraj_hru()

def boj_s_drakem():
    print("\nStojíte tváří v tvář drakovi.")
    print("Jakým způsobem se rozhodnete bojovat?")
    print("1. Použijete meč")
    print("2. Využijete svou sílu")
    print("3. Použijete magii")

    volba = int(input("Zadejte číslo volby: "))

    if volba == 1:
        boj_s_mecem()
    elif volba == 2:
        boj_s_silou()
    elif volba == 3:
        boj_s_magii()
    else:
        print("Neplatný vstup. Zkuste to znovu.")
        boj_s_drakem()

def boj_s_mecem():
    print("\nZvolili jste boj s mečem.")
    vitezne_cislo = random.randint(1, 3)
    tip_cisla = int(input("Zadejte číslo od 1 do 3: "))

    if tip_cisla == vitezne_cislo:
        print("Zasáhli jste draka mečem a zachránili princeznu!")
        vyhra()
    else:
        print("Drak vás přemohl. Hra končí.")
        prohra()

def boj_s_silou():
    print("\nZvolili jste boj se svou silou.")
    sila_hrace = random.randint(1, 10)
    sila_draka = random.randint(1, 10)

    if sila_hrace > sila_draka:
        print("Vaše síla přemohla draka a zachránili jste princeznu!")
        vyhra()
    elif sila_hrace < sila_draka:
        print("Bohužel, drak byl silnější než vy. Hra končí.")
        prohra()
    else:
        print("Vaše síly se vyrovnaly a boj skončil nerozhodně. Co budete dělat?")
        print("1. Pokusíte se o ústup")
        print("2. Pokusíte se o další souboj")

        volba = int(input("Zadejte číslo volby: "))

        if volba == 1:
            print("Ústupíte a hra končí.")
            prohra()
        elif volba == 2:
            print("Opětovně se pustíte do boje.")
            boj_s_silou()
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            boj_s_silou()

def boj_s_magii():
    print("\nZvolili jste boj s magií.")
    magicka_sila_hrace = random.randint(1, 10)
    magicka_sila_draka = random.randint(1, 10)

    if magicka_sila_hrace > magicka_sila_draka:
        print("Vaše magická síla přemohla draka a zachránili jste princeznu!")
        vyhra()
    elif magicka_sila_hrace < magicka_sila_draka:
        print("Drak ovládl silnější magii než vy. Hra končí.")
        prohra()
    else:
        print("Vaše magické síly se vyrovnaly a boj skončil nerozhodně. Co budete dělat?")
        print("1. Použijete magický předmět")
        print("2. Snažíte se o útěk")

        volba = int(input("Zadejte číslo volby: "))

        if volba == 1:
            print("Použijete magický předmět a získáte převahu nad drakem.")
            vyhra()
        elif volba == 2:
            print("Snažíte se o útěk, ale drak vás dostihne. Hra končí.")
            prohra()
        else:
            print("Neplatný vstup. Zkuste to znovu.")
            boj_s_magii()

def vyhra():
    print("\nGratulujeme! Zachránili jste princeznu a vyhráli jste hru.")

def prohra():
    print("\nBohužel, jste poraženi. Princezna zůstává v zajetí draka.")

zahraj_hru()
