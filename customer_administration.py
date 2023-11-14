import phonenumbers
from customer import Customer


class CustomerAdministration:
    """         1. Add new customer
                2. Print all customers
                3. Find customer
    """

    def __init__(self):
        self.customer_list = []  # prehled zakazniku

    def start(self, selection):
        if selection == 1:
            self.add_new_customer()

        elif selection == 2:
            self.print_all_customers()

        elif selection == 3:
            self.find_customer()

    def add_new_customer(self):
        # validate _name
        while True:
            try:
                _name = input("Zadejte jméno pojistného:").lower().strip().capitalize()
                if _name.isalpha():
                    break
                    # string zkontroluji jestli obsahuje pouze pismena, pokud ano, tak se vyskočí z cyklu
                else:
                    raise ValueError

            except ValueError:
                print("Nezadali jste pouze písmena pro jméno!, zadejte jej prosím znovu")
                continue

        # validate _surname
        while True:
            try:
                _surname = input("Zadejte příjmení pojistného:").lower().strip().capitalize()
                if _surname.isalpha():
                    break

                else:
                    raise ValueError

            except ValueError:
                print("Nezadali jste pouze písmena pro příjmení!, zadejte jej prosím znovu")
                continue

        # validate _age
        while True:
            try:
                _age = int(input("Zadejte věk:").strip())
                # pokud je věk zadaný správně, tak se vyskočí z cyklu
                if 0 < _age < 150:
                    break
                else:
                    raise ValueError

            except ValueError:
                print("Nezadali jste validní číslo pro věk, zadejte ho prosím znovu")
                continue

        # validate _phone_number
        while True:
            try:
                _phone_number = input("Zadejte telefonní číslo, ve formátu +420775444555:").strip()
                _check_phone_number = phonenumbers.parse(_phone_number)
                # tel. číslo se parseruje pomoci knihovny phonenumbers
                # pokud neni zadano tel. číslo, tak vyskočí výjimka phonenumbers.NumberParseException
                if phonenumbers.is_valid_number(_check_phone_number):
                    break

                else:
                    raise ValueError

            except phonenumbers.NumberParseException:
                print("Nezadali jste správně tel. číslo")
                continue

            except ValueError:
                print("Nezadali jste správně tel. číslo")
                continue

        # vytvori noveho customera  a pridat ho do prehledu zakazniku
        _new_customer = Customer(_name, _surname, _age, _phone_number)
        self.customer_list.append(_new_customer)
        input("Nový pojištěnec byl přidán. Pokračujte libovolnou klávesou..")

    def print_all_customers(self):
        for customer in self.customer_list:
            print(customer, "\n")

        input("Pokračujte libovolnou klávesou...")

    def find_customer(self):
        _search_name = input("Zadejte jméno hledaného:").lower().strip().capitalize()
        _search_surname = input("Zadejte příjmení hledaného:").lower().strip().capitalize()
        _search_output = []
        for count, customer in enumerate(self.customer_list):
            # hleda shodne jmeno a prijmeni a pokud je najde, prida customera do docasne promenne pro vypis
            if customer.name == _search_name and customer.surname == _search_surname:
                _search_output.append(str(customer))

        if _search_output:
            # pokud se nejaka jmena nasla a list neni prazdny, vypise se obsah
            for customer in _search_output:
                print(customer, "\n")
        else:
            print("Hledaný pojištěnec v seznamu není")

        input("Pokračujte libovolnou klávesou..")
