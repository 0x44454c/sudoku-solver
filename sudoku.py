"""
Title: Class for sudoku solver program

@author: Monimoy
Student at GCETTB
"""


class Sudoku:

    def __init__(self):
        print("Welcome to the Sudoku solver!\nMade with ❤ by Monimoy.")

    def solution_finder(self, board, ele_list):  # finds the correct element for the cell

        # checks if the cell is blank
        pos = self.blank_cell(board)
        if not pos:
            return True
        else:
            x, y = pos

        # checks if the value is suitable for the cell
        for i in ele_list:
            if self.ele_checker(board, i, (x, y)):
                board[x][y] = i
                # goes on iteration for checking further suitability of the elements
                if self.solution_finder(board, ele_list):
                    return True

                board[x][y] = '-'

        return False

    def ele_checker(self, board, ele, position):  # checks if the ele present in row or column or box

        # row checker
        for i in range(len(board[position[0]])):
            if board[position[0]][i] == ele and i != position[1]:
                return False

        # column checker
        for i in range(len(board[position[1]])):
            if board[i][position[1]] == ele and i != position[0]:
                return False

        # box checker
        box_div = int(len(board[0]) ** 0.5)
        box_y = position[0] // box_div
        box_x = position[1] // box_div

        for i in range(box_y * box_div, box_y * box_div + box_div):
            for j in range(box_x * box_div, box_x * box_div + box_div):
                if board[i][j] == ele:
                    return False

        return True

    def blank_cell(self, board):  # for finding blank cell
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '-':
                    return i, j  # returns row, column
        return None

    def print_board(self, board):  # for printing the sudoku board
        lenboard = len(board)
        l2 = int(lenboard ** 0.5)
        print('-------------------------')

        for i in range(lenboard):
            if i % l2 == 0 and i != 0:  # prints horizontal separator for boxes
                print('-------------------------')
            for j in range(lenboard):
                if j % l2 == 0:  # prints vertical separator for boxes
                    print('| ', end="")

                # prints the elements of the sudoku board
                if j == lenboard - 1:
                    print(board[i][j], end=" |\n")

                else:
                    print(board[i][j], end=" ")
        print('-------------------------')

    def separator(self, sep, ran):  # used to create an 2d array from user input
        outlist = []
        if sep == '':
            for j in range(ran):
                b = [str(i) for i in input()]
                outlist.append(b)
        else:
            for i in range(ran):
                b = list(map(str, input().split(' ' or ',')))
                outlist.append(b)
        return outlist
