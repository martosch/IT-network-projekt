from customer_administration import CustomerAdministration

selection = None
nova_pojistovna = CustomerAdministration()

while True:
    try:
        # dokud uzivatel nevybere konec, tak se mu po dokonceni akce opet vypise co muze dale delat: selection
        # pokud je zadana blbost, je nutne zadat znovu. Pokud se zada spravne cislo, provede se prislusna metoda.
        selection = int(input("Vyberte možnost: \n 1. Přidat nového pojištěnce\n"
                              " 2. Vypsat všechny pojištěnce\n 3. Najít pojištěnce\n 4. Konec\n "))

        if selection == 4:
            break

        if 0 < selection < 4:
            new_selection = nova_pojistovna.start(selection)

        else:
            raise ValueError

    except ValueError:
        print("Nezadali jste správné číslo, zadejte ho prosím znovu:")
        continue

print("Nashledanou")