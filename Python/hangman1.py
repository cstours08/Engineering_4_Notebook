#Hangman/Challeng thing
#Written by Corin Saint Ours

from time import sleep
import os
wrong = 0

# Player 1 word request
word = input("Player 1, type in the secret word: ")
length = len(word) #determines the length of a given word and gives it a 
#assgined term, pretty cool
secret = list(word)
sleep(2)
os.system('clear')
val = word
spaces = ['_'] * length

#prints the hangman  as mistakes are made
def msp (x):
  msp = [" 0 "]
  if x >= 2:
    msp.append(" |")
  if x >= 3:
    msp.append(" |")
  if x >= 4:
    msp.append("/")
  if x >= 5:
    msp.pop()
    msp.append("/ \\")
  if x >= 6:
    msp.pop(1)
    msp.insert(1, "\\|")
  if x == 7:
    msp.pop(1)
    msp.insert(1, "\\|/")
  print(*msp, sep="\n")

while "_" in spaces and wrong < 7:
  print(spaces)
  cue2 = input("Player 2, please guess a letter: ")

  try:
    pos = [i for i in range(len(secret)) if secret[i] == cue2]
    #finds if a letter is in range of the secret word more then once
    point = 0
    val4 = len(pos)
    while val4 > 1 and val4 != point:
      spaces[pos[point]] = cue2
      point = point + 1
    spaces[pos[0]] = cue2

  except:
    print("You are incorrect")
    wrong = wrong+1
    msp(wrong)
else:
 print(spaces)
 if wrong < 7:
    print("Congratulations!")
 print("Game over")
 print("The correct word was: " + word)
