class Customer:
    # jmeno, prijmeni, vek, telefon
    def __init__(self, name: str, surname: str, age: int, phone_number: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_nuber = phone_number

    def __str__(self):
        return str(self.name + " " + self.surname + " " + str(self._age) + " " + self.phone_nuber + " " + self.adulthood)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value):
        # setter na vek, abychom si ulozili dodatečnou informaci o plnoletosti
        self._age = new_value
        # kontrola jestli je plnolety
        if new_value >= 18:
            self.adulthood = "dospělý"

        else:
            self.adulthood = "dítě"
