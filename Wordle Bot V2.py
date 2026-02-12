# Wordle Bot - Find  efficient words to guess while playing Wordle

import re
from collections import defaultdict

# Get the official list of answers and guesses
answerWords = []
with open("wordleAnswers.txt", "r") as file:
    for answer in file:
        answer = answer.strip("\n")
        answerWords.append(answer)

guessWords = []
with open("wordleGuesses.txt", "r") as file:
    for guess in file:
        guess = guess.strip("\n")
        guessWords.append(guess)

# Make a list for the possible answers that will be changed later
possibleAnswers = answerWords

amountOfGuesses = 6

print("Welcome to WordleBot, this bot will help you find the best words to guess when playing wordle!")

# Guesses Loop
while amountOfGuesses > 0:

    # Pass in the guess
    playerGuess = (input("Type your guess:")).lower()

    # Check if the guess is valid
    if len(playerGuess) != 5:
        print("Guess doesn't equal 5 characters")
        continue
    elif bool(re.search(r'[^a-zA-Z]', playerGuess)):
        print("Guess isn't valid")
        continue
    elif playerGuess not in guessWords:
        print("Guess isn't valid")
        continue

    # Pass in the pattern _ = Gray, ~ = Yellow, O = Green
    pattern = input("Type the pattern:")

    # Check if the pattern is valid
    if len(pattern) != 5:
        print("Pattern doesn't equal 5 characters")
        continue
    elif bool(re.search(r'[^~_O]', pattern)):
        print("Pattern isn't valid")
        continue
    elif pattern == "OOOOO":
        print("You've won!")
        break

    patternColors = []

    # Assign pattern values to colors
    for color in pattern:
        match color:
            case "_":
                patternColors.append("Gray")
            case "~":
                patternColors.append("Yellow")
            case "O":
                patternColors.append("Green")

    squareIndex = 0
    grayLetters = []
    yellowLetters = defaultdict(list)
    greenLetters = defaultdict(list)
    requiredCounts = defaultdict(int)

    # Assign colors to each letter of the player's guess

    for square in patternColors:
        letter = playerGuess[squareIndex]

        if square == "Gray":
            grayLetters.append(letter)

        elif square == "Yellow":
            yellowLetters[letter].append(squareIndex)
            requiredCounts[letter] += 1

        elif square == "Green":
            greenLetters[letter].append(squareIndex)
            requiredCounts[letter] += 1

        squareIndex += 1

    # Remove/keep words based on color

    for word in possibleAnswers[:]:
        removeWord = False

        # Check if word is in required counts and if it isn't remove it
        wordLetterCounts = {}
        for letter in word:
            wordLetterCounts[letter] = wordLetterCounts.get(letter, 0) + 1

        for letter, count in requiredCounts.items():
            if wordLetterCounts.get(letter, 0) < count:
                removeWord = True
                break

        if removeWord:
            possibleAnswers.remove(word)
            continue

        for letter, positions in greenLetters.items():
            for pos in positions:
                if word[pos] != letter:
                    removeWord = True
                    break

        if removeWord:
            possibleAnswers.remove(word)
            continue

        for letter, positions in yellowLetters.items():
            for pos in positions:
                if word[pos] == letter:
                    removeWord = True
                    break

        if removeWord:
            possibleAnswers.remove(word)
            continue

        for letter in grayLetters:
            if letter not in requiredCounts and letter in word:
                removeWord = True
                break

        if removeWord:
            possibleAnswers.remove(word)

    letterOccurrences = {"a": 0, "b": 0, "c": 0, "d": 0,
                         "e": 0, "f": 0, "g": 0, "h": 0,
                         "i": 0, "j": 0, "k": 0, "l": 0,
                         "m": 0, "n": 0, "o": 0, "p": 0,
                         "q": 0, "r": 0, "s": 0, "t": 0,
                         "u": 0, "v": 0, "w": 0, "x": 0,
                         "y": 0, "z": 0, }
    for word in possibleAnswers[:]:
        for letter, letterFrequency in letterOccurrences.items():
            if letter in word:
                letterFrequency += 1
                letterOccurrences[letter] = letterFrequency

    # Sorting the dictionary by values in descending order
    sortedLetterOccurrences = dict(sorted(letterOccurrences.items(), key=lambda item: item[1], reverse=True))

    bestLetters = list(sortedLetterOccurrences.keys())

    print("The best letters are: ", end="")
    for bestLetter in bestLetters:
        print(f"{bestLetter}, ", end="")
    print("")

    bestWords = []
    '''
        for word in possibleAnswers:
            for letter in bestLetters:
                if letter not in greenLetters and letter not in yellowLetters:
                    if letter in word and word not in bestWords:
                        bestWords.append(word)
    '''

    # Score words based on amount of common letters
    wordScores = {}

    for word in possibleAnswers:
        score = 0
        uniqueLetters = set(word)

        for letter in uniqueLetters:
            if letter not in greenLetters and letter not in yellowLetters:
                score += letterOccurrences[letter]

        wordScores[word] = score

    # Sort words by score
    bestWords = sorted(wordScores, key=wordScores.get, reverse=True)

    wordRank = 1
    for word in bestWords:
        print(f"The number {wordRank} word is {word}, ", end="")
        wordRank += 1

    print("")

    amountOfGuesses -= 1
