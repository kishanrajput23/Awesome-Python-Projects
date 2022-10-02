**Kevin** and **Stuart** want to play the **'The Minion Game'**.

### Game Rules :
- Both players are given the same string, S.
- Both players have to make substrings using the letters of the string S.
- Stuart has to make words starting with consonants.
- Kevin has to make words starting with vowels.
- The game ends when both players have made all possible substrings.

### Scoring :
A player gets +1 point for each occurrence of the substring in the string S.

### Example :
- String S = BANANA

![image](https://user-images.githubusercontent.com/105034758/193463925-fd4630b4-25a5-4141-9fb0-babe1c2aabe2.png)

### Input Format :
- A single line of input containing the string S.
- The string S will contain only uppercase letters:[A - Z] .

### Constraints :
0 < len(s) <= 10^6

### Output Format :
- Print one line: the name of the winner and their score separated by a space.
- If the game is a draw, print Draw.
