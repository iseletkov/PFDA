class Checkers:
    def __init__(self):
        field = """
            XBXBXBXB
            BXBXBXBX
            XBXBXBXB
            XXXXXXXX
            XXXXXXXX
            WXWXWXWX
            XWXWXWXW
            WXWXWXWX
        """.replace('\n', '').replace('\r', '').replace(' ', '')
        ind = 0
        self.cells = {}
        for row in '87654321':
            self.cells[row] = {}
            for col in 'ABCDEFGH':
                self.cells[row][col] = Cell(field[ind])
                ind += 1

        return

    def get_cell(self, pos):
        """
            self - ссылка на текущий экземпляр данного класса.
            pos - строчка из двух символов, обозначающая координаты ячейки, которую надо получить.
        """
        if pos[0] not in 'ABCDEFGH':
            return None
        if pos[1] not in '87654321':
            return None

        return self.cells[pos[1]][pos[0]]

    def move(self, f, t):
        if f[0] not in 'ABCDEFGH':
            return
        if f[1] not in '87654321':
            return 
        if t[0] not in 'ABCDEFGH':
            return
        if t[1] not in '87654321':
            return  

        cell_from = self.get_cell(f)
        # Если пытаемся ходить шашкой из ячейки, в которой шашки нет - ничего не делаем.
        state_from = cell_from.status()
        if state_from == "X":
            return

        cell_to = self.get_cell(t)
        # Если целевая ячейка не пустая, ход не делаем.
        if cell_to.status() != "X":
            return

        # Если нет рубки, то целевая ячейка должна раполагаться по диагонали на одну клетку от исходной. 

        # Изменяем состояние исходной ячейки на пустое.
        cell_from.set_state("X")
        
        cell_to.set_state(state_from)
        center_row = ""
        center_column = ""
        if ord(t[0])-ord(f[0]) == 2 and ord(t[1])-ord(f[1]) == 2:
            center_row = chr(ord(t[1])-1)
            center_column = chr(ord(t[0])-1)
        if ord(t[0])-ord(f[0]) == -2 and ord(t[1])-ord(f[1]) == 2:
            center_row = chr(ord(t[1])+1)
            center_column = chr(ord(t[0])-1)
        if ord(t[0])-ord(f[0]) == 2 and ord(t[1])-ord(f[1]) == -2:
            center_row = chr(ord(t[1])-1)
            center_column = chr(ord(t[0])+1)
        if ord(t[0])-ord(f[0]) == -2 and ord(t[1])-ord(f[1]) == -2:
            center_row = chr(ord(t[1])+1)
            center_column = chr(ord(t[0])+1)

        if center_row != "":
            cell_center = self.get_cell(center_column+center_row)
            # Надо ещё проверить, что фигура там принадлежит противоположному игроку.
            cell_center.set_state("X")

        # Могут быть ещё и каскадные ходы.   


class Cell:

    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state

    def set_state(self, state):
        if state not in 'XWB':
            return  
        self.state = state


checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
checkers.move('D4', 'E5')
checkers.move('F6', 'D4') # Здесь рубка
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()

# print (chr(ord("A")+1))