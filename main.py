from words import words
import random
import string

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or " " in word:
    word = random.choice(words)
  return word.upper()  
                        
def hangman():
  word = get_valid_word(words)
  cword = set(word)
  alphabet =  set(string.ascii_uppercase)
  used_letters = set()
  lives = 6

  while len(cword)>0 and lives>0:
    print("You have", lives, "lives left. The used alphabets are ", " ".join(used_letters))
    word_list = [letter if letter in used_letters else "-" for letter in word]
    print("The word is ", " ".join(word_list))
    user_input = input("Enter the new alphabet: ").upper()
    if user_input in alphabet - used_letters:
      used_letters.add(user_input)
      if user_input in cword:
        cword.remove(user_input)
      else:
        lives = lives - 1
    elif user_input in used_letters:
      print("You have already used this letter. Please try again.")
    else:
      print("Invalid character. Please try again.")
  
  if lives == 0:
    print("You died!, the word was", word)
  else:
    print("Congrats! The word was", word)
    
hangman()  