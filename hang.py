import random
from words import words #import words that are going to be used


def choose_word():
    word = random.choice(words) #choose a random word from words.py
    return word.upper()


def play(word):
  wordc = "_"* len(word)
  guess = false
  guessl =[]
  guessw = []
  tries = 6
  print("hangman")
  print(display_hangman(tires))
  print(wordc)
  print("\n")
  #loop of guess word 
  while not guess and tries > 0:
    guess = input("letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in guessl:
          print("you already choose that letter or word",guess)
        elif guess not in word:
          print(guess, "wrong")
          tries -= 1
          guessl.append(guess)
        else:
          print("nice", guess, "is correct")
          guessl.append(guess)
          word_as_list = list(wordc)
          indices = [i for i, letter in  enumerate(word) if letter == guess]
          for index in indices:
            word_as_list[index] =  guess
          wordc = "".join (word_as_list)
          if "_" not in wordc:
            guess = True
    elif leng(guess) == len(word) and guess.isalpha():
      if guess in guessw:
        print("wrong", guess)
      elif guess != word:
        print(guess, "wrong")
        tries -= 1
        guessw.append(guess)
      else:
          guess = True
          wordc = word 
    else:
      print("wrong")
      print(display_hangman(tries))
      print(wordc)
      print("\n")
    #no more tries
  if guess:
    print("you won")
  else:
  print("you lost the word was" + word + "try again")

  def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]




#put everything togheter
def main():
word = get_word()
play(word)
#play again
while input("play again (y/n)").upper() == "y":
word =get_word()
play(word)
if __name__=="_main_":
main()  
  pass


  