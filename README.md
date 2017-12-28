# LastMouseLost
Computer Implementation of Board Game called 'Last Mouse Lost' from www.FoxMind.com

# Instructions
The files needed to run the newest version of the game are 'last_mouse_lost.py', 'player.py' and 'board.py'. Run 'last_mouse_lost.py' with python in console to play the game.

The object of the game is to not select the last dot. You want your opponent to select the last dot on the board in order to win. The game doesn't allow you to make invalid moves. You can select as many as you want from one row, you must select at least one dot and the dots you select must be from the same row. Input a row number and an amount of dots you want to select.

If you would like to play against another human player turn by turn or play a random player, in the '__main__' block of 'last_mouse_lost.py', change the parameters of 'g.run_game' where the first argument is the number of human players, the second is the number of random players and the third is number of smart players.

---

#### Below is the description of how the game AI actually works. The entire 'AI Minimax Approach' section is now irrelevant as to how the code works since I no longer use the Minimax algorithm to choose moves but instead an algorithm I created using the 'Mirror Strat'. Although the Minimax approach is not how the game is implmented if you wish to fully understand how and why the Mirror Strat works it is recommended you read the Minimax approach, the Note and the Mirror Strat section of this README

---

## AI Minimax Approach

The first approach I trook to this game was the use the minimax algorithm to calculate the best move by the computer. This strategy worked to some degree in giving better moves than a random player but did not always choose a perfect move. The time required to run this algorithm was also quite lengthy with some turns taking minutes to compute a move.

In order to cut down the runtime I began to use the games design to my advantage.

  1. Symmety in the board:
    The board is symmetrical so making a move on the top row of 3 or the bottom row of three does not make a difference if both rows contain same amount of dots. For example in the first turn making move [0, 2] is equivalent to move [5, 2] (in this example the notation used is [row, amount of dots]).
    This idea can be taken a step further since the symmetry is not just for rows with the same maximum length. For example if any two rows have 2 dots the moves between those rows are identical.
    This allowed me to cut down the board combinations since you can have many boards that share the same total number of dots in each row but the dots may be in different rows. For example boards were stored in the format of a dictionary where the key is the number of dots and the value is the number of rows with those amount of dots.
    
    Example: {0: 2, 1: 2, 3: 1, 4: 1} is a representation of all the boards shown below:
    
        x x x        |        x x o        |        x x x
      x x x x o      |      x x x x o      |      x x o o o
     x x o o o o     |     x x x x x x     |     x x x x x o
     x x x o o o     |     x x x x x x     |     x x o o o o
      x x x x o      |      x o o o o      |      x x x x x
        x x x        |        o o o        |        x x o
        
  2. Counting backwards in board:
    Since for almost all of the board operations the only thing we care about is how many dots are available, we don't care about the number of x's but only about the number of o's. Therefore instead of having a for loop that counts from 0 to the length of the row, the for loops were changed to count backwards from the length of the row to the first 'x'. This allowed the loop to stop earlier taking much less time when you account for the fact that these functions were being called thousands of times whenever nodes were created.
    
    Example: The row 'x x x o o o' would take 6 steps to find that there are 3 available dots if we count from 0 to length of row, but only takes 4 steps to count from length of row to the first 'x' (3 steps for each 'o' and 1 step for the 'x' to break for loop)
    
  3. Winning boards
    When I first played this game I began to gain an interest into the strategy when I began to notice that certain board combinations would gurantee a win. For example the easiest board combination that guarantees you win is {0: 5, 1: 1}. This is a winning board since I can guarantee I will win if I aim to make this the board on my opponents turn (this example is obvious since with only one dot my opponent must choose the only available dot and I will win). However there are many other more complicated boards you can find that will guarantee a win if you play the most optimal move, {0: 3, 1: 1, 2: 1, 3: 1}, {0: 4, 3: 2} and {0: 1, 1: 1, 2: 1, 3: 3} are some examples (the first two are easyt to play out and become intuitive, the last one may not seem intuitive as to why it guarantees a win however this is because no matter what move your opponent makes you can get to another winning board in one move). In the board class within 'board.py' there is a list of winning boards that are organized by how many rows of 0 there are (This is no longer in the newest version that uses the strat but if you view the previous commits you can view the old 'board.py' with the total list of ones I have found).
    By using these winning boards you could cut down the tree of this functions calculated moves since once you hit one of these boards you did not have to compute all the moves after since you know that you can always win at this state. This shortened the runtime since you no longer had to calculate the board combinations down to a single dot.

---

These 3 game mechanics allowed me to cut down the runtime of this function and try to optimize it. This did speed up the decision making time along with some other tricks however I could not get it to become a reasonable time to compute moves.

---

#### Note before next section
##### This Note will only make sense if you have read the part above about the minimax algorithm. This note will explain how I discovered the 'mirror strat' described below.

As I developed the minimax algorithm for this program I played against the computer for quite some time and as I played I began to find new winning boards that I could add to my list for the computer to use. As I did so I began to notice a pattern with some of the winning boards. It seemed that if you took the sum of two winning boards the result would also become a winning board (Not 100% sure this works for all boards | by sum I mean {0: 4, 3: 2} + {0: 4, 2: 2} = {0: 2, 2: 2, 3: 2}, i.e you replace the empty rows of one winning board with the second winning board). So I now had a hypothesis that by summing any two winning boards you would result with a new winning board (once again I had no evidence to prove this but I could not find a counter example to my theory | additionally I have a rough 'proof' in my head as to why this would be the case and I think I understand why this might be true, however that proof is not necessary or relavent to my program).

With this knowledge I began to try some combinations of winning boards and found that many of the very simple winning boards could be summed to fill most of the board. For example I knew that if you had 4 empty rows and 2 rows with the same number of dots (greater than 1) it was a winning board. This meant I could take the board {0: 4, 3: 2} and {0: 4, 5: 2} and result with a sum of {0: 2, 3: 2, 5: 2}. This board is a winning board consisting of rows 0, 1, 4, 5 filled with rows 2, 3 empty. This made me think about how possibly if I took {0: 4, 3: 2} + {0: 4, 5: 2} + {0: 4, 6: 2} I could get a winning board that consisted of every dot!! The long story short is that yes, the entire board is a winning board!! So I had just discovered if the person who made the second move made the optimal move every turn, they would always win. Moving first would guarantee a loss if you played against a perfect player.

Naturally, I made my program such a perfect player that will always make a perfect move*. That results in what I have dubbed the 'mirror strat'. This is because it turns out that the optimal move for almost all of the board, is to just copy the move of your opponent. For all moves (up until the end where you have to play a bit more carefully to not to shoot yourself in the foot) if you mirror your opponent you are making the optimal move*.

Now this became kind of anti-climactic ending since I have now just beaten the game of Last Mouse Lost. There is a perfect move from the very beginning of the game where if you go second you will always* win. There is not much strategy left to the game for me since I know every possible best move that will win me the game and I know if I have won before my first move is made.

That is an explanation as to how I came up with the strategy and my process in perfecting the game of Last Mouse Lost.

Below there is a further explanation of how the 'mirror strat' works in contrast to this note explaning how I discovered it.

---

## Mirror Strat

###### The reasoning behind the strategy is shown above in the 'Note' but requires you read the 'Minimax approach' first to understand the 'Note'.

This strategy as the name implies has the computer mirror the user's move for most of the game. For example if the first move is [0, 2] the computer will decide to move [5, 2] (once again using the [row, amount of dots] notation). This mirroring occurs for most of the game until one of 2 situations occurs. These situations are shown as 2 if statements within the 'move' function of SmartPlayer.

1. (3 ones + one other row) or (5 ones + one other row) or (1 one + one other row)
  In this case you want to remove all dots from the row with the most dots, this will result in either the board {0: 3, 1: 3} or {0: 1, 1: 5} or {0: 5, 1: 1} respectively. Each of these boards will have rows each containing one dot. There is an odd amount of rows which is necessary to ensure the opponent is forced to push the last dot.
  
2. (2 ones + one other row) or (4 ones + one other row) or (one row of some amount of dots)
  This case is very similar to the case above. The only difference is that instead of taking all the dots from the max row, it leaves one dot. This results in the same outcome as in case 1 since you are essentially just adding another row with one dot.
  
If neither of these cases are fulfilled then the computer will mirror the player until one of these scenarios occur. These scenarios are needed since if they were not in place then the other opponent could just take a row every turn and the computer would delete the last row and lose, or the player could also be a bit smarter and try to outplay the computer however these two cases prevent that.

Therefore the Mirror Strat can be used to guarantee a win if you are the second player in the game.

---

\* when I say optimal move or always win, I have no formal proof that this will always win the game however I have run over a million games where a smart player plays the random player using the mirror strat and the smart player never loses. Therefore I feel confident in saying it will always win and I don't see a flaw with the strategy
