import random
import hangmanWordlist



#wordlist = ["mousee" , "dogo" , "att"]

chosen_word = random.choice(hangmanWordlist.wordlist)
display = []
lives = 6

# Creating a list with ["-"]
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    user_letter = input("Enter the letter? ")

    #checks the letter if in word and at the position
    for position in range(len(chosen_word)):
        if chosen_word[position] == user_letter:
            display[position] = user_letter

    if user_letter not in chosen_word:
        lives -=1
        print(f"Lives left {lives}")
        if lives == 0:
            end_of_game = True
            print("User loose")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("User won")
