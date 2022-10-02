# minesweeper

This is a Python implementation of 2-D Minesweeper!

You start a game by running the script:
```
python3 minesweeper.py
```
(If you do not edit the parameters in the script, the script will automatically initialize it to a 10x10 board, with 10 bombs)

Note that the inputs must be that the number of bombs is less than the total number of spaces (n^2).

For now, this script does not have a GUI and you can use terminal :D (If you want to make a GUI, feel free to make a pull request)

In order to "dig" at a certain location, you type in the index of the row, then the column, separated by a comma (whitespace optional). The game "digs" recursively around that location if there are no bombs nearby.

You can continue digging until either you hit a bomb (which is game over) or you've successfully dug up all n-b non-bomb locations (which is victory)!

![Screenshot 2022-10-02 133600](https://user-images.githubusercontent.com/104320194/193444718-59c460c7-de14-4c3c-af3e-e0a9735bafc9.jpeg)
![Screenshot 2022-10-02 133612](https://user-images.githubusercontent.com/104320194/193444725-59b7bac0-3be2-43f3-b612-f619d2edd0c3.jpeg)
