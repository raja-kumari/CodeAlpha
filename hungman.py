import random

word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)  # test purpose only

display = []
for letter in chosen_word:
    display.append('_')

game_over = False

while not game_over:
    print(' '.join(display))
    guessed_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!")

    if '_' not in display:
        game_over = True
        print("You win!")
