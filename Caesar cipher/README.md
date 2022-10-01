# Caesar cipher 
The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique.
It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. 

Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down.

Examples :
Text : ATTACKATONCE
Shift: 4
Cipher: EXXEGOEXSRGI

Algorithm for Caesar Cipher: 
Input: 

1. A String of lower case letters, called Text.
2. An Integer between 0-25 denoting the required shift.