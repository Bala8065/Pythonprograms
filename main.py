#Guess the Random number

import random


number = (random.randint(1,100))
print(number)
attempts = 0


print("Guess the number between 1 and 100 !!!!!!")


while True:
   guess = int(input("Enter your guess:"))
   attempts += 1


   if guess > number:
       print("Too high. try again")
   elif guess < number:
       print("Too low. try again")
   else:
       print(f"Congratulation!!!, you guessed correct number in {attempts} attempts")


       break


#Word scramble

import random

words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]

def word_scrambled(word):
    word_scrambled = ''.join(random.sample(word, len(word)))
    return word_scrambled

score = 0
attempts = 0

while True:
    selected_word = random.choice(words)
    max_attempts = 3

    while attempts < max_attempts:
        guess = input("Guess the scrambled word: " + word_scrambled(selected_word))

        if guess == selected_word:
            score += 1
            attempts += 1
            print("Correct! You guessed the word in " + str(attempts) + " attempts.")
            break

        else:
            attempts += 1
            print("Incorrect. Try again.")

    if attempts == max_attempts:
        print("Game Over! You ran out of attempts. The correct word was: " + selected_word)
        break

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        print("Thank you for playing! Your final score is: " + str(score))
        break

