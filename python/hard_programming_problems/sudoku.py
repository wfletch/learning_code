from math import floor
import timeit
from wsgiref.util import guess_scheme
def solveSudoku(board):
        """
        Do not return anything, modify board in-place instead.
        """
        # Ok, let's figure this out. it''s a backtracking problem
        MAX_Y = len(board)
        MAX_X = len(board[0])
        def _valid_x_values(y):
            # Given a current y position, return all the x values
            found_values = []
            for x in range(0,9):
                if board[y][x] != ".":
                    found_values.append(int(board[y][x]))
            # Ok, we have the numbers which already exist, let's get the ones we can use!
            return [x for x in range(1,10) if x not in found_values]
        def _valid_y_values(x):
                # Given a current y position, return all the x values
                found_values = []
                for y in range(0,9):
                    if board[y][x] != ".":
                        found_values.append(int(board[y][x]))
                # Ok, we have the numbers which already exist, let's get the ones we can use!
                return [y for y in range(1,10) if y not in found_values]
        def _valid_cell_values(y,x):
            start_y, start_x = int(floor(y/3)), int(floor(x/3))
            state = board[start_y*3][start_x*3: start_x*3 + 3] + board[start_y*3 +1][start_x*3: start_x*3 + 3] + board[start_y*3 + 2][start_x*3: start_x*3 + 3]
            state = [int(y) for y in state if y != "."]
            return [y for y in range(1,10) if y not in state]
        number_of_plays = sum([board[y][x] == "." for y in range(MAX_Y) for x in range(MAX_X)])
        guess_count = 1
        def _backtrack(number_of_plays):
            nonlocal guess_count
            guess_count +=1
            if number_of_plays == 0:
                # We are done as there are no more numbers to play
                return True
            else:
                # We still have numbers to play
                for y in range(MAX_Y):
                    for x in range(MAX_X):
                        if board[y][x] != ".":
                            continue
                        # We need to get the list of all numbers we could use
                        valid_x = _valid_x_values(y)
                        valid_y = _valid_y_values(x)
                        valid_cell = _valid_cell_values(y,x)
                        # print(y,x)
                        # print (valid_x, valid_y, valid_cell)
                        # valid numbers is the intersection of all 3
                        valid_values = [y for y in range(1,10) if y in valid_cell and y in valid_x and y in valid_y]
                        if valid_values == []:
                            return False
                        # if we do not have any valid values, we should stop
                        for val in valid_values:
                            # Ok, so we should be doing something now
                            board[y][x] = str(val)
                            if (_backtrack(number_of_plays-1)):
                                return True
                            board[y][x] = "."
                        return False
        _backtrack(number_of_plays)
        print(guess_count)
if __name__ == "__main__":
    board = [[".",".",".","7",".",".",".",".","."],["1",".",".",".",".",".",".",".","."],[".",".",".","4","3",".","2",".","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","5",".","9",".",".","."],[".",".",".",".",".",".","4","1","8"],[".",".",".",".","8","1",".",".","."],[".",".","2",".",".",".",".","5","."],[".","4",".",".",".",".","3",".","."]]
    solveSudoku(board)
    for i in board:
        print (i)
