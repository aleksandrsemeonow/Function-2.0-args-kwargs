class Contact:

    def __init__(self, name, surname, number, favorite_contact=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favorite_contact = favorite_contact
        self.args = args
        self.kwargs = kwargs
        for passion in self.args:
            print('-', passion)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Номер телефона: {self.number}\n' \
               f'В Избранных: {self.favorite_contact}\n' \
               f'Дополнительная информация: \n\t{self.kwargs}'


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
sam = Contact('Sam', 'Brooks', '+78757392920', favorite_contact='да', telegram='@sam', email='sam@brooks.ru')



class Phonebook:

    def __init__(self, name):
        self.name = name
        self.contacts = dict()

    def add_number(self, contact, name):
        self.contacts[name] = contact

    def find_number(self, surname):
        for name in self.contacts:
            if surname in self.contacts[name].name or surname in self.contacts[name].surname:
                print(self.contacts[name])

    def delete_number(self, number):
        for name in self.contacts:
            if number in self.contacts[name].number:
                del self.contacts[name]
                break

    def find_favorite_contact(self):
        for name in self.contacts:
            if self.contacts[name].favorite_contact!=False:
                print(self.contacts[name])

    def __str__(self):
        return str(self.contacts)


if __name__ == '__main__':
    phonebook = Phonebook('sasha')
    phonebook.add_number(jhon, 'Джон')
    phonebook.add_number(sam, 'Сэм')
    # phonebook.find_favorite_contact()
    phonebook.delete_number('+71234567809')
    # phonebook.find_number('Jhon')
    print(phonebook)
