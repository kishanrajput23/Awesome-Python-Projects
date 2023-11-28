# Sudoku solver
Sudoku solver using backtracking

Basically in sudoku, we want to be able to solve a sudoku puzzle given an input like this, 
which represents a sudoku board:
```
[[x00, x01, x02, x03... x08],
 [x10, x11, x12, x13... x18],
 ...
 [x80, x81, x82, x83... x88]]
```
These x_rc values correspond to the value at the rth row, cth column (starting with 0-index)
These values could be empty (we will represent this with -1)

So for example,
```
[[-1,  1,  5, ...],
 [-1, -1, -1, ...],
 [ 6, -1, -1, ...]
 ...]
```
would represent a board like this:
```
 -----------
|     1   5 | ...
|           | ...
| 6         | ...
 -----------
 ...
```
Now, our goal is to solve our sudoku puzzle using Python! :D

![image](https://user-images.githubusercontent.com/104320194/193804587-780cb986-dbb2-4119-83ad-605f1b03d1fa.png)
