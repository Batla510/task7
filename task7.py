
class Reader:
    def __init__(self, fio, n, f, dr, p, x, y):
        self.fio = fio
        self.n = n
        self.f = f
        self.dr = dr
        self.p = p
        self.x = x
        self.y = y
    def taB(self):
        print(self.fio, 'взял', self.x, 'книгу')
    def returnBook(self):
        print(self.fio, 'вернул', self.y, 'книг')
pers1 = Reader('Петров В.В.', '8756', 'учебный', '29/12/2005', '89648388932', 5, 5)
pers1.takeBook()
pers1.returnBook()