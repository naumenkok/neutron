class Color:
    red = 0
    white = 1
    neutron = 2
    empty = 3


class Board: 
    def __init__(self):
      self.board = [[Empty()] * 5 for y in range(5)]
      self.board[2][2] = Piece(Color.neutron)
      for x in range(5):
        self.board[0][x] = Piece(Color.red)
        self.board[4][x] = Piece(Color.white)   

    def get_color(self, x, y):
        return self.board[y][x].color

    def check(self):
        pass

    def move(self):
        pass

        
    def play(self):
        # print (f'Start')
        # x_str, y_str = input("Enter the coordinates of the piece you want to move(x y):").split()
        # x = int(x_str) - 1
        # y = int(y_str) - 1
        pass


    def __str__(self):
        result = '   1 2 3 4 5  '
        for i in range(5):
            result += "\n" + f"{i + 1} " + ''.join(map(str, self.board[i])) + f" {i + 1}"
        result += "\n" + '   1 2 3 4 5 '
        print(result)


class Piece:
    IMG = ('🔴', '⚪', '⭐')

    def __init__(self, color):
        self.color = color

    def variants_of_moving(self, board, x, y):
        pass

    def __str__(self):
        if self.color == Color.red:
            return self.IMG[0]
        elif self.color == Color.white:
            return self.IMG[1]
        else:
            return self.IMG[2]
        

class Empty:
    color = Color.empty

    def variants_of_moving(self, board, x, y):
        raise Exception('Error !')

    def __str__(self):
        return ' +'


b = Board()
b.__str__()