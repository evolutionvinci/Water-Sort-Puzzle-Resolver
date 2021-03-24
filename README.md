# Water-Sort-Puzzle-Resolver
A simple resolver for the game "Water Sort Puzzle" (https://play.google.com/store/apps/details?id=com.gma.water.sort.puzzle&amp;hl=it&amp;gl=US)  
  How to use it:  
  Download this repo and open the input.txt file, fill it with numbers following this rule.
  Start from the top left container then the the container on its right till the end and then the bottom left till the last full container on the bottom right (dont put      zeros for empty containers, there is a variable inside water.py called EmptyContainer, on line 6, change his value to the number of empty containers).
  For every conteiner, from top to bottom, associate a number to a color, the first color you meet is 1 the second different color is 2...
  Put all the numbers on the same line divided by a single space (" ").
  Then run the program from terminal with this command: python water.py < input.txt
  Wait till the program finishes the execution, At the end follow all the steps from bottom to top, you'll see all the containers on the same line and the numbers are the colors you assigned before, zeros are empty spaces, and the colors in blue are the move you have to replicate. 
