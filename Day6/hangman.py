import random
from hangman_art import logo
from hangman_art import stages


from hangman_words import word_list
# word_dict = ['zebra', 'elephant', 'snake']
# chosen_word = random.choice(word_list)
lives = 6
end_of_lives = False
selected_word = random.choice(word_list)

hidden_letters = []
replaced_word = selected_word

for xx in range(len(selected_word)):
    x = random.randrange(0, len(selected_word))
    if selected_word[x] not in hidden_letters:
        hidden_letters.append(selected_word[x])
        replaced_word = replaced_word.replace(selected_word[x], "_")

print(logo)
print("Guess the letter ", replaced_word)
replaced_word_list = list(replaced_word)
already_guessed = []
hit = 0
for i in range(lives):
    if (len(hidden_letters) != hit):
        guessed_letter = input("Guess the letter: ").lower()
        if guessed_letter in already_guessed:
            print(stages[lives])
            lives = lives - 1
            print(
                f"You alread guessed {guessed_letter.upper()}. You lose a life.")
        elif guessed_letter in hidden_letters:
            print("right")
            hit = hit + 1
            position = selected_word.index(guessed_letter)
            print(position)
            replaced_word_list[position] = guessed_letter
            already_guessed.append(guessed_letter)
            print(replaced_word_list)
        else:
            print(stages[lives])
            lives = lives - 1
            already_guessed.append(guessed_letter)
            print(
                f"You guessed {guessed_letter.upper()}, that's not in the word. You lose a life.")
    else:
        print("Yes you have saved the Hangman!",  replaced_word_list)
