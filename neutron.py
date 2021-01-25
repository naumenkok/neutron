from random import choice


class Color:
    red = 0
    white = 1
    neutron = 2
    empty = 3


class Board: 
    def __init__(self):
        self.board = [[Empty()] * 5 for y in range(5)]
        # self.board[1][3] = Piece(Color.neutron)
        # for x in range(5):
        self.board[1][0] = Piece(Color.red)
        self.board[0][1] = Piece(Color.red)
        self.board[0][2] = Piece(Color.red)
        self.board[0][3] = Piece(Color.red)
        self.board[0][4] = Piece(Color.red)

        self.board[4][0] = Piece(Color.white) 
        self.board[4][1] = Piece(Color.white) 
        self.board[2][0] = Piece(Color.white) 
        self.board[4][3] = Piece(Color.white) 
        self.board[4][4] = Piece(Color.white)   


    def get_coordinates(self, color_number):
        list_of_coordinates = []
        for x in range(5):
            for y in range(5):
                if self.board[y][x].color == color_number:
                    x_n_ = x
                    y_n_ = y
                    list_of_coordinates.append([x_n_, y_n_])
        return list_of_coordinates

    def get_color(self, x, y):
        return self.board[y][x].color

    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def check_move(self, list_of_moves, move):
        if move in list_of_moves:
            return True
        else:
            print(f'You cannot move a pawn to this place')
            return False

    def check_result(self, x, y):
        color_number_for_neutron = 2
        if self.get_color(x, y) == color_number_for_neutron:
            if y == 0:
                print(f'Red win!!!')
                return True
            elif y == 4:
                print(f'White win!!!')
                return True
            else:
                return False

    def check_amount_of_moves(self, variants_of_moves):
        if variants_of_moves == []:
            return True
        else:
            return False

    def check_type_of_pawn(self, x, y, modulo):
        color_number_for_red = 0
        color_number_for_white = 1
        color_number_for_neutron = 2
        if modulo == 0 and self.get_color(x, y) != color_number_for_white:
            print('You enter incorreсt coordinates')
            return False
        if ((modulo == 1) or (modulo == 3)) and (self.get_color(x, y) != color_number_for_neutron):
            print('You enter incorreсt coordinates')
            return False
        if modulo == 2 and self.get_color(x, y) != color_number_for_red:
            print('You enter incorreсt coordinates')
            return False
        else:
            return True

    def enter_coordinates(self, position):
        if position == 0:
            text = f'Enter coordinates of the piece you want to move (x y):'
        elif position == 1:
            text = f'Enter coordinates where you want to move to (x y):'
        inp = input(text).split()
        if len(inp) == 2:
            if all(map(lambda c:c.isdigit(), inp)):
                x_from_str, y_from_str = inp
                x = int(x_from_str) - 1
                y = int(y_from_str) - 1
                return x, y
            else:
                print('You enter incorreсt coordinates')
                return False    
        else:
            print('You enter incorreсt coordinates')
            return False

    def enter_and_check(self, position, param=None):
        bool_flag = False
        while not bool_flag:
            try:
                x, y = self.enter_coordinates(position)
                if position == 0:
                    bool_flag = self.check_type_of_pawn(x, y, param)
                elif position == 1:
                    bool_flag = self.check_move(param, [x, y])
            except:
                print('You enter incorreсt coordinates')
                bool_flag = False
        return x, y

    def choose_coordinates_from_list(self, color_number, position, variants_of_moves=None):
        if position == 0:
            list_of_coordinates = self.get_coordinates(color_number)
            [x, y] = choice(list_of_coordinates)
        elif position == 1:
            [x, y] = choice(variants_of_moves)
        return x, y

    def choose_type_of_game(self):
        inp = "0"
        while (inp != "1") and (inp != "2"):
            inp = input("Enter number:")
        return int(inp)

    def get_coord_from(self, inp, modulo, from_position):
        if (inp == 2) and (modulo == 2):
            x_from, y_from = self.choose_coordinates_from_list(0, from_position)
        elif (inp == 2) and (modulo == 1):
            x_from, y_from = self.choose_coordinates_from_list(2, from_position)
        else:
            x_from, y_from = self.enter_and_check(from_position, modulo)
        return x_from, y_from

    def get_coord_to(self, inp, modulo, to_position, variants_of_moves):
        if (inp == 2) and (modulo == 2):
            x_to, y_to = self.choose_coordinates_from_list(0, to_position, variants_of_moves)
        elif (inp == 2) and (modulo == 1):
            x_to, y_to = self.choose_coordinates_from_list(2, to_position, variants_of_moves)
        else:
            x_to, y_to = self.enter_and_check(to_position, variants_of_moves)
        return x_to, y_to

    # def variant_rec(self, x_n, y_n, depth=1, path=[]):
    #     if depth == 4:
    #         return []
    #     # variants = self.board[y_n][x_n].variants_of_moving_all(self, x_n, y_n)
    #     variants = Piece(Color.neutron).variants_of_moving_all(self, x_n, y_n, dict={})
    #     for x in range(5):
    #         if ([x, 4] in variants) and (depth != 2):
    #             dict[(x, 4)]=100
    #             return path
    #     for variant in variants:
    #         path.append([x_n, y_n])
    #         self.variant_rec(variant[0], variant[1], depth + 1, path)

    def probability_of_winning(self, x_n, y_n, dict_d1={}):
        variants = Piece(Color.neutron).variants_of_moving_all(self, x_n, y_n)
        # self.board[x_n][x_n] = Piece(Color.empty)
        for x in range(5):
            if [x, 4] in variants:
                dict_d1[(x, 4)]={}
                dict_d1[(x, 4)][1]=1
                variants.remove([x, 4])
                # return dict_d1
        for variant in variants:
            dict_d1[(variant[0], variant[1])]={}
            variants_d2 = Piece(Color.neutron).variants_of_moving_all(self, variant[0], variant[1])
            number_of_m = len(variants_d2)
            dict_d1[(variant[0], variant[1])][number_of_m]=0
            for x in range(5):
                if [x, 4] in variants_d2:
                    dict_d1[(variant[0], variant[1])][number_of_m] += 1
                    variants_d2.remove([x, 4])
            for variant_d2 in variants_d2:
                variants_d3 = Piece(Color.neutron).variants_of_moving_all(self, variant_d2[0], variant_d2[1])
                for x in range(5):
                    if [x, 4] in variants_d3:
                        dict_d1[(variant[0], variant[1])][number_of_m] += 1
        # self.board[x_n][x_n] = Piece(Color.neutron)
        return dict_d1
                

            

    def play(self):
        print('Start. Select game mode: 1-man and man. 2-man and fool computer')
        inp = self.choose_type_of_game()
        self.__str__()
        bool_result = False
        number_of_move = 0
        while not bool_result:
            from_position = 0
            to_position = 1
            modulo = number_of_move % 4

            x_from, y_from = self.get_coord_from(inp, modulo, from_position)
            variants_of_moves = self.board[y_from][x_from].variants_of_moving_all(self, x_from, y_from)
            bool_result = self.check_amount_of_moves(variants_of_moves)
            if bool_result:
                quit() 
            
            x_to, y_to = self.get_coord_to(inp, modulo, to_position, variants_of_moves)
            
            computer_move = input("Press Enter for move")
            if number_of_move == 0:
                print('First move')
            else:
                print('Next move')
            self.__str__()
            print()
            self.move([x_from, y_from], [x_to, y_to])
            self.__str__()
            bool_result = self.check_result(x_to, y_to)
            number_of_move += 1

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

    def check_start_position(self, moves, x, y):
        start_position = [x, y]
        while start_position in moves:
            moves.remove(start_position)
        return (moves)

    def variants_of_moving_diagonal(self, board, x, y):
        moves = []
        for i in (-1, 1):
            for j in (-1, 1):
                moves_diag = self.loop_for_variants(board, moves, x, y, i, j)
        return moves_diag

    def variants_of_moving_all(self, board, x, y):
        moves_diag = self.variants_of_moving_diagonal(board, x, y)
        for j in (-1, 1):
            i = 0
            moves_ver_diag = self.loop_for_variants(board, moves_diag, x, y, i, j)
            moves_hor_ver_diag = self.loop_for_variants(board, moves_ver_diag, x, y, j, i)
        moves_all = moves_hor_ver_diag   
        self.check_start_position(moves_all, x, y) 
        # print(moves_all)        
        return moves_all
    
    def loop_for_variants(self, board, moves, x, y, i, j):
        x_i = x + i
        y_j = y + j
        while (0 <= x_i <= 4) and (0 <= y_j <= 4):
            color = board.get_color(x_i, y_j)
            if color != Color.empty:
                break
            x_i += i
            y_j += j
        moves.append([x_i - i, y_j - j])
        return moves  

    def __str__(self):
        pict = (
            self.IMG[0] if self.color == Color.red 
            else self.IMG[1] if self.color == Color.white 
            else self.IMG[2] 
        )
        return pict
        

class Empty:
    color = Color.empty

    def variants_of_moving_all(self, board, x, y):
        return []

    def __str__(self):
        return ' +'
