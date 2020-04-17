"""
Title: Sudoku solver
@author: Monimoy
Student at GCETTB


One example of Sudoku to enter:

53--7----
6--195---
-98----6-
8---6---3
4--8-3--1
7---2---6
-6----28-
---419--5
----8--79

"""

from sudoku import *
import time


def initiator(su):
    order = int(input('\nEnter the order of the sudoku:\n'))
    sep = input("Please choose separator: comma(,)/space( )/none(enter)\n")
    print('Enter the elements of the sudoku:\ne.g. 123456789 for 9 order sudoku')
    ele = su.separator(sep, 1)
    print('Enter the sudoku with blank as - (hypen):')
    board = su.separator(sep, order)

    # prints the entered sudoku
    print("Entered Sudoku:")
    su.print_board(board)

    # solving start
    start = time.time()
    su.solution_finder(board, *ele)
    print("Solved sudoku:")
    su.print_board(board)
    print("Solved in ", round(time.time() - start, 4), " second!")


def main():
    su = Sudoku()
    initiator(su)

    while True:
        dec = input("\nDo you want to solve another sudoku? Y/y\n")
        if dec in ['Y', 'y']:
            initiator(su)
        else:
            print('Thank you for using Sudoku solver!')
            break


main()
