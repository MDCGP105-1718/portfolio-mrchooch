from random import choice
from os import system
from string import ascii_lowercase
from time import sleep

#Imports a bunch of words
import json
with open("words.json") as data_file:    
    wordList = json.load(data_file)

def startGame():
    global hangpart,chosenWord,chosenWordDisp,guesses,wrongLetters,playerGuess

    hangpart=[" "," "," "," "," "," "," "," "," "]
    guesses=0

    chosenWord=choice(wordList["data"])

    wrongLetters=[]
    chosenWordDisp=[]
    for i in range(len(chosenWord)):
        chosenWordDisp.append(".")  

    drawBoard()

def drawBoard():
    global hangpart,chosenWord,chosenWordDisp,guesses,wrongLetters,playerGuess

    system("cls")
    print(" %s    \n"      %(hangpart[1]),
          "%s   %s    \n"  %(hangpart[0],hangpart[2]),
          "%s   %s    \n"  %(hangpart[0],hangpart[3]),
          "%s  %s%s%s   \n"%(hangpart[0],hangpart[5],hangpart[4],hangpart[6]),
          "%s  %s %s   \n" %(hangpart[0],hangpart[7],hangpart[8]),
          "%s        \n"   %(hangpart[0]),
          "=========\n\n",
          "%s\t\t%s\n"%("".join(chosenWordDisp),",".join(wrongLetters)))
   
    if "".join(chosenWordDisp) == chosenWord:
        print("---Game Over---\nYou Win\n")
        sleep(1)
        restartQuestion = input("Play Again?: ").lower()
        if restartQuestion == "y" or restartQuestion == "yes":
            startGame()
        else:
            exit()

    if guesses==9:
        print("---Game Over---\nYou Lose\n\nThe word was %s"%(chosenWord))
        sleep(1)
        restartQuestion = input("Play Again?: ").lower()
        if restartQuestion == "y" or restartQuestion == "yes":
            startGame()
        else:
            exit()   
  
   
    playerGuess = input("Enter Guess: ")

    if playerGuess not in ascii_lowercase or playerGuess == "":
        drawBoard()


    playGame()

def playGame():
    global hangpart,chosenWord,chosenWordDisp,guesses,wrongLetters,playerGuess

    if playerGuess in list(chosenWord):
        indexOfLetter = [i for i in range(len(chosenWord)) if chosenWord[i] == playerGuess]
        for i in range(len(indexOfLetter)):
            chosenWordDisp[indexOfLetter[i]] = playerGuess   
    else:
        if playerGuess not in wrongLetters:
            guesses += 1
            wrongLetters.append(playerGuess)

    if guesses == 1:
        hangpart[0] = "|"
    elif guesses == 2:
        hangpart[1] = "+---+"
    elif guesses == 3:
        hangpart[2] = "|"
    elif guesses == 4:
        hangpart[3] = "0"
    elif guesses == 5:
        hangpart[4] = "|"
    elif guesses == 6:
        hangpart[5] = "/"
    elif guesses == 7:
        hangpart[6] = "\\"
    elif guesses == 8:
        hangpart[7] = "/"
    elif guesses == 9:
        hangpart[8] = "\\"

    drawBoard()
    
startGame()
input()
