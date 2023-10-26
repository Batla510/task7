class CPerson:
    def __init__(self, name,surname,otch,data,pol):
        self.name = name
        self.surname = surname
        self.otch = otch
        self.data = data
        self.pol = pol

    def rd(self):
        print(f"Имя: {self.name} \n" 
              f"Фамилия: {self.surname} \n" 
              f"Отчество: {self.otch} \n" 
              f"Дата рождения: {self.data} \n" 
              f"Пол: {self.pol} \n")

    def ch(self,name,surname,otch,data,pol):
        print(f"Имя: {self.name} \n"
              f"Фамилия: {self.surname} \n"
              f"Отчество: {self.otch} \n"
              f"Дата рождения: {self.data} \n"
              f"Пол: {self.pol} \n")


    def __del__(self):
        print('Всё стёрто')
tom = CPerson('alex', 'fef', 'ser',17012007,'m')
tom.rd()
tom.ch('alex', 'fef', 'ser',17012007,'m')