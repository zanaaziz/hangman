# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:55:45 2017

@author: Zana Daniel
"""

import random

wordList = ["ELON MUSK", "STEVE JOBS", "BILL GATES", "LARRY PAGE", "CHARLES RANLETT FLINT", "JEFF BEZOS", "NICOLAUS COPERNICUS", "ALBERT EINSTEIN", "ALAN TURING"]
wordListSecret = ["**** ****", "***** ****", "**** *****", "***** ****", "******* ******* *****", "**** *****", "******** **********", "****** ********", "**** ******"]
wordHints = ["Arguably the most influential man of the past decade or two, owner of many revolutionary companies.",
             "A great visionary that changed the tech industry to what it is today. May he RIP.",
             "The man who dominated the computer world.",
             "The co-founder of a service which we can never live without even for a day.",
             "Founder of one of the top IT companies of all time.",
             "Created biggest store in the history of mankind.",
             "A physicist who challenged the way we viewed the world.",
             "Known as the greatest mind in human history.",
             "When a computer is smart enough, they'll take this gentlemans test."
             ]

word = random.choice(wordList)
wordIndex = wordList.index(word)
    
# how to play
def tutorial():
    print("\nWelcome to Hangman in Python!\nYou will be given a hint and you may guess one letter at a time.\nRemember, you only have 10 lives!\n")
    
# the main function
def start():
    lives = 10
    print("Lives: ", str(lives))
    print("Hint:\n" + wordHints[wordIndex], "\n")
    print(wordListSecret[wordIndex])
    
    while "*" in wordListSecret[wordIndex] and lives > 0:
        guess = input("Enter a letter to guess.\n").capitalize()
        
        for i in range(0, len(word)):
            if word[i] == guess:
                wordListSecret[wordIndex] = wordListSecret[wordIndex][:i] + guess + wordListSecret[wordIndex][i + 1:]
            
        if guess not in word:
            lives -= 1
            print("\nWrong guess.\nLives: ", str(lives))
            print("Hint:\n" + wordHints[wordIndex])
        else:
            print("\nYou've already guessed that letter!")
        
        print("\n" + wordListSecret[wordIndex])
    
    # this is for when the while condition becomes false    
    else:
        if lives <= 0:
            print("\nYou have lost...\n")
        else:
            print("\nCongratulations you win with " + str(lives) + " lives remaining!!!\n")
    

tutorial()
start()