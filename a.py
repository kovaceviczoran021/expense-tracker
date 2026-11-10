from pathlib import Path
def napravi(path):
    path.mkdir(parents=True, exist_ok=True)
    path = path / "troskovi.txt"
    path.touch(exist_ok = True)
    return path

def upisi(trosak, cena, path):
    with open(path, "a") as file:
        file.write(f"{trosak}|{cena}\n")

def cene(path):
    lista = []
    with open(path, "r") as file:
        for linija in file:
            rec = linija.split("|")
            lista.append(float(rec[1]))
    return lista

def troskovi(path):
    lista = []
    with open(path, "r") as file:
            for linija in file:
                rec = linija.split("|")
                lista.append(rec[0])
    return lista


def ukupno(lista_cena):
    ukupna_cena = 0
    for broj in lista_cena:
        ukupna_cena += broj
    return ukupna_cena

def izlistaj(lista_troskova, lista_cena):
    for i in range(len(lista_troskova)):
        print(f"{lista_troskova[i]}:{lista_cena[i]}")


def najveci(lista_cena, lista_troskova):
    najveca_cena = 0
    nova = []
    if len(lista_cena) == 0:
        return ("Nema unetih troskova!")
    for i in range(len(lista_cena)):
        if lista_cena[i] > najveca_cena:
            najveca_cena = lista_cena[i]
    for i, cena in enumerate(lista_cena):
        if cena == najveca_cena:
            nova.append(lista_troskova[i])
    if len(nova) == 1:
        return(f"Najveci trosak je \'{nova[0]}\' i iznosi: {najveca_cena}")
    else:
        return(f"Najveci trosak od {najveca_cena} imaju: {", ".join(nova)}!")

def pronadji(lista_troskova, lista_cena, a):
    brojac = 0
    for i, trosak in enumerate(lista_troskova):
        if trosak == a:
            print(f"Trosak za {trosak} iznosi: {lista_cena[i]}")
            brojac += 1
    print(f"Pronadjeno je {brojac} troskova sa nazivom {a}!")

def prosek(suma, broj):
    if broj == 0:
        return "Nema unetih troskova!"
    prosecna_cena = suma/broj
    return (f"Prosecna cena po trosku je: {prosecna_cena}")

def obrisi(path, naziv):
    nova = []
    with open(path, "r") as file:
        lista = file.readlines()
        for linija in lista:
            rec = linija.split("|")
            if rec[0] != naziv:
                nova.append(linija)
    with open(path, "w") as file:
        for linija in nova:
            file.write(linija)
def izmeni(path, naziv, nova_cena):
    nova = []
    with open(path, "r") as file:
        for linija in file:
            rec = linija.split("|")
            if rec[0] != naziv:
                nova.append(linija)
            else:
                rec[1] = str(nova_cena)
                nova.append("|".join(rec)+"\n")
    with open(path, "w") as file:
        for linija in nova:
            file.write(linija)



if __name__ == "__main__":
    path = Path(__file__).resolve().parent / "troskovi"
    path = napravi(path)
    while True:
        print("---------APLIKACIJA ZA PRACENJE TROSKOVA---------")
        print("1. Dodaj trosak")
        print("2. Prikazi listu troskova")
        print("3. Prikazi ukupnu potrosnju")
        print("4. Pronadji odredjeni trosak")
        print("5. Obrisi odredjeni trosak")
        print("6. Izmeni cenu")
        print("7. Najveci trosak")
        print("8. Prosek troskova")
        print("0. Izlaz")
        lista_cena = cene(path)
        lista_troskova = troskovi(path)
        izbor = input("Izaberite opciju: ")
        match izbor:
            case "1":
                print("Dodavanje troskova:")
                while True:
                    trosak = input("Unesite naziv troska: ").strip().lower()
                    if trosak == 'prekini':
                        break
                    if not trosak:
                        print("Naziv troska ne sme biti prazan!")
                        continue
                    if "|" in trosak:
                        print("Naziv ne sme sadrzati karakter \'|\'")
                        continue
                    while True:
                        try: 
                            cena = float(input("Unesite cenu tog troska: "))
                            if cena < 0:
                                print("Cena ne sme biti manja od nule, upisite ponovo!")
                                continue
                            break
                        except ValueError:
                            print("Morate uneti broj!")
                    upisi(trosak, cena, path)
            case "2":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Lista troskova:")
                    izlistaj(lista_troskova, lista_cena)
            case "3":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Ukupna potrosnja: ")
                    suma = ukupno(lista_cena)
                    print(f"Ukupni troskovi su: {suma}")
            case "4":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Cena odredjenog troska: ")
                    while True:
                        while True:
                            a = input("Unesite naziv troska kome zelite da proverite cenu: ").strip().lower()
                            if not a:
                                print("Morate upisati nesto!")
                                continue
                            break
                        if a == 'prekini':
                            break
                        if a not in lista_troskova:
                            print("Uneli ste nepostojeci trosak!")
                            continue
                        pronadji(lista_troskova, lista_cena, a)
            case "5":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Brisanje odredjenog troska: ")
                    while True:
                        while True:
                            b = input("Unesite naziv troska koji zelite da obrisete: ").strip().lower()
                            if not b:
                                print("Morate upisati nesto!")
                                continue
                            break
                        if b == 'prekini':
                            break
                        if b not in lista_troskova:
                            print("Uneli ste nepostojeci trosak!")
                            continue
                        obrisi(path, b)
                        lista_cena = cene(path)
                        lista_troskova = troskovi(path)
            case "6":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Izmeni cenu: ")
                    while True:
                        while True:
                            c = input("Unesite naziv troska kome zelite da promenite cenu: ").strip().lower()
                            if not c:
                                print("Morate upisati nesto!")
                                continue
                            break
                        if c == 'prekini':
                            break
                        if c not in lista_troskova:
                            print("Uneli ste nepostojeci trosak!")
                            continue
                        while True:
                            try:
                                nova_cena = float(input(f"Unesite novu cenu za {c}: "))
                                if nova_cena < 0:
                                    print("Cena ne sme biti negativna!")
                                    continue
                                break
                            except ValueError:
                                print("Morate uneti broj!")
                                continue
                        izmeni(path, c, nova_cena)
                        lista_cena = cene(path)
                        lista_troskova = troskovi(path)
            case "7":
                if not lista_troskova:
                    print("Nema unetih troskova")
                else:
                    print("Najveci trosak: ")
                    print(najveci(lista_cena, lista_troskova))
            case "8":
                suma = ukupno(lista_cena)
                if lista_troskova:
                    print("Prosek troskova: ")
                    print(prosek(suma, len(lista_troskova)))
                else:
                    print("Nema unetih troskova!")
            case "0":
                print("Dovidjenja!")
                break
            case _:
                print("Nepostojeca opcija!")