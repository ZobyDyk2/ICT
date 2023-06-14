import random

def zahraj_hru():
    print("Vítejte ve hře 'Záchrana princezny'!")
    print("Princezna je unesena zlým drakem.")
    print("Vaším úkolem je projít několika místnostmi a zachránit princeznu.")

    while True:
        mistnosti = [
            {"název": "Temný les", "možnosti": ["Hluboká propast", "Mýtiny", "Stezka rovně"], "výhra": False},
            {"název": "Horská jeskyně", "možnosti": ["Rozcestí vpravo", "Rozcestí vlevo"], "výhra": True},
            {"název": "Starý hrad", "možnosti": ["Použít klíč", "Rozkopnout dveře"], "výhra": True},
            {"název": "Magický pramen", "možnosti": ["Napít se z pramene", "Prohlédnout si pramen"], "výhra": True}
        ]

        print("\nVyberte si jednu z místností: ")
        for i, mistnost in enumerate(mistnosti):
            print(f"{i + 1}. {mistnost['název']}")

        volba = int(input("Zadejte číslo místnosti: ")) - 1
        if volba < 0 or volba >= len(mistnosti):
            print("Neplatný vstup. Zkuste to znovu.")
            continue

        mistnost = mistnosti[volba]
        print(f"\nJste v {mistnost['název']}.")

        if mistnost['výhra']:
            vyhra()
        else:
            print("Vidíte před sebou několik možností:")
            for i, možnost in enumerate(mistnost['možnosti']):
                print(f"{i + 1}. {možnost}")

            volba = int(input("Zadejte číslo možnosti: ")) - 1
            if volba < 0 or volba >= len(mistnost['možnosti']):
                print("Neplatný vstup. Zkuste to znovu.")
                continue

            možnost = mistnost['možnosti'][volba]
            if "drak" in možnost.lower():
                boj_s_drakem()
            else:
                print("\nNemůžete tímto směrem pokračovat.")
                hraj()

def boj_s_drakem():
    print("\nStojíte tváří v tvář drakovi.")
    print("Jakým způsobem se rozhodnete bojovat?")
    print("1. Použijete meč")
    print("2. Využijete svou sílu")
    print("3. Použijete magii")

    volba = int(input("Zadejte číslo volby: "))

    if volba == 1:
        if random.randint(1, 3) == 1:
            print("Zasáhli jste draka mečem a zachránili princeznu!")
            vyhra()
        else:
            print("Drak vás přemohl. Hra končí.")
            prohra()
    elif volba == 2:
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
            volba = int(input("1. Pokusíte se o ústup\n2. Pokusíte se o další souboj\nZadejte číslo volby: "))

            if volba == 1:
                print("Ústupíte a hra končí.")
                prohra()
            elif volba == 2:
                print("Opětovně se pustíte do boje.")
                boj_s_drakem()
            else:
                print("Neplatný vstup. Zkuste to znovu.")
                boj_s_drakem()
    elif volba == 3:
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
            volba = int(input("1. Použijete magický předmět\n2. Snažíte se o útěk\nZadejte číslo volby: "))

            if volba == 1:
                print("Použijete magický předmět a získáte převahu nad drakem.")
                vyhra()
            elif volba == 2:
                print("Snažíte se o útěk, ale drak vás dostihne. Hra končí.")
                prohra()
            else:
                print("Neplatný vstup. Zkuste to znovu.")
                boj_s_magii()
    else:
        print("Neplatný vstup. Zkuste to znovu.")
        boj_s_drakem()

def vyhra():
    print("\nGratulujeme! Zachránili jste princeznu a vyhráli jste hru.")

def prohra():
    print("\nBohužel, jste poraženi. Princezna zůstává v zajetí draka.")

zahraj_hru()
