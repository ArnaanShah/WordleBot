# WordleBot 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/01e0107f-1ad2-4523-bada-bb8444f02449" />

Welcome to WordleBot! WordleBot is a tool designed to help players make efficient guesses while playing Wordle. The bot looks at the pattern, and then narrows down the list of possible answers and ranks the best next guesses based on letter frequency.

## How to use

***Lets do an example using the word STERN as our answer***

1. You will be greeted and then prompted to enter a guess.

```
Welcome to WordleBot, this bot will help you find the best words to guess when playing wordle!
Type your guess:
```

2. Type in the first word you want to guess. (Not case-sensitive)

```
Welcome to WordleBot, this bot will help you find the best words to guess when playing wordle!
Type your guess: Stare
```

3. You will now be prompted to enter the pattern. To do this, guess your word in Wordle and then type out the 5 letter pattern.

**Type it using this format: _ = Gray, ~ = Yellow, O = Green**

```
Welcome to WordleBot, this bot will help you find the best words to guess when playing wordle!
Type your guess: Stare
Type the pattern:OO_O~
```

4. Then, the bot will return the list of best letters and words to guess in descending order. (You can ignore the best letters if you don't want to make your own guesses)

```
Welcome to WordleBot, this bot will help you find the best words to guess when playing wordle!
Type your guess: Stare
Type the pattern:OO_O~
The best letters are: e, n, r, s, t, a, b, c, d, f, g, h, i, j, k, l, m, o, p, q, u, v, w, x, y, z, 
The number 1 word is stern,
```

5. After this, choose a word from the list and enter it into wordle. If going for the highest score, choose the first answer. Otherwise, choose a word you like! 

6. Finally, the program will loop and you will be prompted to enter a guess again.

### HAVE FUN!
