import random

def generovat_otazku():
    """Generuj náhodný matematicý příklad."""
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
    
        x = y * random.randint(1, 5)
    otazka = f"{x} {operator} {y}"
    return otazka

def ohodnotit_odpoved(otazka, odpoved):
    """Ohodnotí, zda odpověď uživatele je správná."""
    try:
        spravna_odpoved = eval(otazka)
        if float(odpoved) == spravna_odpoved:
            return True
    except:
        pass
    return False

def main():
    spravne = 0
    for _ in range(10):
        otazka = generovat_otazku()
        print("Otázka:", otazka)
        uzivatelska_odpoved = input("Tvoje odpověď: ")
        if ohodnotit_odpoved(otazka, uzivatelska_odpoved):
            print("Ty jsi ale šikulka máš to správně!")
            spravne += 1
        else:
            print("Nenene hlupáčku máš to špatně.")
    
    print(f"\nVypočítal jsi {spravne} z 10 otázek správně.")

if __name__ == "__main__":
    main()