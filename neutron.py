class MyError(Exception):
    pass


class Color:
    red = 0
    white = 1
    neutron = 2
    empty = 3


class Board: 
    def __init__(self):
      self.board = [[Empty()] * 5 for y in range(5)]
      self.board[2][1] = Piece(Color.neutron)
      for x in range(5):
        self.board[0][x] = Piece(Color.red)
        # self.board[4][x] = Piece(Color.white)   

    def get_color(self, x, y):
        return self.board[y][x].color

    def move(self, yx_from, yx_to):
        self.board[yx_to[0]][yx_to[1]] = self.board[yx_from[0]][yx_from[1]]
        self.board[yx_from[0]][yx_from[1]] = Empty()

    def check(self):
        pass
        
    def play(self):
        print (f'Start')
        self.__str__()
        # for move in range(1, 7):
        #     x_from_str, y_from_str = input("Enter coordinates of the piece you want to move (x y):").split()
        #     x = int(x_from_str) - 1
        #     y = int(y_from_str) - 1
        #     if move == 1 and y != 4 and y != 0:
        #         print(f'You enter wrong coordinates. Try again.')
        #     yx_from = [y, x]
            
            
        #     x_to_str, y_to_str = input("Enter coordinates where you want to move to (x y):").split()
        #     x = int(x_to_str) - 1
        #     y = int(y_to_str) - 1
        #     yx_to = [y, x]
            
        #     self.__str__()
        #     print(f'                   .')
        #     self.move(yx_from, yx_to)
        #     self.__str__()


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

    def variants_of_moving_diagonal(self, board, x, y):
        moves = []
        for a in (-1, 1):
            c = x + a
            b = y + a
            while (0 <= c <= 4) and (0 <= b <= 4):
                color = board.get_color(c, b)
                if color != Color.empty:
                    break
                b += a
                c += a
            moves.append([c-a, b-a])
        start_position = [x, y]
        if start_position in moves:
            moves.remove(start_position)
        print(moves)

    def variants_of_moving_diagonal_2(self, board, x, y):
        moves = []
        for a in (-1, 1):
            c = x + a
            b = y - a
            while (0 <= c <= 4) and (0 <= b <= 4):
                color = board.get_color(c, b)
                if color != Color.empty:
                    break
                b -= a
                c += a
            moves.append([c-a, b+a])
        start_position = [x, y]
        if start_position in moves:
            moves.remove(start_position)
        print(moves)

    def variants_of_moving_straight(self, board, x, y):
        moves = []
        for j in (-1, 1):
            i = y + j
            while 0 <= i <= 4:
                color = board.get_color(x, i)
                if color != Color.empty:
                    break
                i += j
            moves.append([x, i-j])
        for j in (-1, 1):
            i = x + j
            while 0 <= i <= 4:
                color = board.get_color(i, y)
                if color != Color.empty:
                    break
                i += j
            moves.append([i-j, y])
        start_position = [x, y]
        if start_position in moves:
            moves.remove(start_position)
        print(moves) 

    def __str__(self):
        pict = (
            self.IMG[0] if self.color == Color.red 
            else self.IMG[1] if self.color == Color.white 
            else self.IMG[2] 
        )
        return pict
        

class Empty:
    color = Color.empty

    def variants_of_moving(self, board, x, y):
        raise Exception('Error !')

    def __str__(self):
        return ' +'
   

b = Board()
b.play()

p = Piece(Color.neutron)
p.variants_of_moving_diagonal(b, 1, 2)
p.variants_of_moving_diagonal_2(b, 1, 2)
p.variants_of_moving_straight(b, 1, 2)