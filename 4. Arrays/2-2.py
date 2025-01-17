# Tic-Tac-Toe is a simple yet fun game for two players.
# You play on a grid of nine squares arranged in three rows
# and three columns.

# The array below shows a Tic-Tac-Toe board.
# Write a program that prints a board on the screen.

# 3x3 Tic-Tac-Toe board
# 3x3 Tablica przedstawiająca planszę do gry w "Kółko-krzyżyk" (Tic-Tac-Toe)
tic_tac_toe_board = [
   ['X', 'O', 'X'],  # Pierwszy rząd: X, O, X
   [' ', 'X', 'O'],  # Drugi rząd: puste pole, X, O
   ['O', ' ', 'X']   # Trzeci rząd: O, puste pole, X
]

# Pętla przechodząca przez każdy wiersz planszy
for row in tic_tac_toe_board:
    # Pętla wewnętrzna przechodzi przez każdą kolumnę w danym wierszu
    for column in row:
        # Drukuje każdą komórkę w danym wierszu, oddzieloną spacją
        print(column, end=" ")
    # Po wydrukowaniu całego wiersza przechodzi do nowej linii
    print()
