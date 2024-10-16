
import random
from hangmanlogo import stages
from hangmanwordlist import word_list

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
end_of_game=False
word_lenght = len(chosen_word)
lives=6
display = []
for _ in range(word_lenght):
    display+="_" 
print(display)  
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life.")
        lives-=1   
        if lives==0:
            end_of_game=True
            print("YOU LOSE.")
            print(f'Pssst,the solution is {chosen_word}.')
    print(f"{' '.join(display)}")  
    if "_" not in display:
        end_of_game=True 
        print('YOU WIN')
        print(f'Pssst,the solution is {chosen_word}.')
    print(stages[lives])    
        


