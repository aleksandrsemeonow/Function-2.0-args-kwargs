
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

    def write_to_data(self):
        with open('data.txt', 'w') as file:
            file.write(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Номер телефона: {self.number}\n'
               f'В Избранных: {self.favorite_contact}\n'
               f'Дополнительная информация: \n\t{self.kwargs}')

    def main(self):
        self.write_to_data()

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(Contact)
jhon.main()


        