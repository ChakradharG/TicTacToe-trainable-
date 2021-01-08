# TicTacToe_Trainable
A tictactoe playing bot that implements trial and error method wherein whenever it loses, it deletes the last (wrong) move it made from the list of possible moves. If only 1 move is possible for that particular board then the cpu deletes the previous move (i.e., it backtracks).

At the time of upload, 1 have trained the code in excess of 1200 games. But it would take round about 10,000 games
to learn all the moves.


T3_Final is the actual game which imports the T3_Core file.
T3_board contains all possible combinations of the board.
T3_do contains the corresponding possible moves for the current state of board.
T3_winratio contains win/loss details, 1 means the cpu won/tie and 0 means it lost.

<br>

## Getting Started
* Clone this repository
* Run ```T3_Final.py```
