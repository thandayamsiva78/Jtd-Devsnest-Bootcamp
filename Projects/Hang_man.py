# Hang Man Game

# player 1
name= input("Enter your name:::")
print(f"Hello, {name}")
print("Let's play the HANGMAN GAME")
# Generate a word
word=["apple","banana","cherry","mango","grapes"]
fin_word=int(input("Select from 0 to 4 ::"))
print("clue:::It is a fruit")
selected_word=word[fin_word]
# print(selected_word)

# Generate a blanks as well as the word length
my_list = []
for i in selected_word:
    my_list += '_'
print(my_list)

# player 2
# guess a letter
chances = 5
while True:
    guessed_letter = input("Your Guess::").lower()
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guessed_letter:
            my_list[position] = guessed_letter
    print(my_list)

    if guessed_letter not in selected_word:
        chances -= 1
        print(chances,"chances left")
        print("try again.....")
        if chances == 0:
            print("<<<<<<<<<<<<<<<<<<<YOU LOSE>>>>>>>>>>>>>>>>>>>>>>>>")
            break

    if '_' not in my_list:
        print("<<<<<<<<<<<<<CONGRATULATIONS>>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<YOU WON>>>>>>>>>>>>>>>>>>>>>>")
        break





# # HangMan Game
# # import HangMan_stages
# name=input("Enter you name::")
# print(f"Hii {name}")
# print("Let's start the  HANGMAN  Game ")
# # Generate Words
# words=["lion","tiger","monkey","bear","kangaroo"]
# find_word=int(input("Select a letter from 0 to 4:"))
# selected_word=words[find_word]  # string
# # print(selected_words)

# # Generate a blanks as well as words length
# my_list=[]
# for i in range(len(selected_word)):
#     my_list += '_'
# print(my_list)
# chances = 6
# # Guess the letter
# game_over = False
# while not game_over:
#     guessed_letter=input("Guess a letter::").lower()
#     for position in range(len(selected_word)): # apple =>len(5)
#         letter = selected_word[position]  # apple[1 to 5]
#         if letter == guessed_letter: # apple[1 to 5] == "a"
#             my_list[position] = guessed_letter  # ['_', '_', '_', '_', '_']=[1 to 5] = "a"[0]
#     print(my_list)
#     if guessed_letter not in selected_word:
#         chances -=1
#         print(chances,"chances left")
#         if chances == 0:
#             game_over = True
#             print("<<<<<You lose!!>>>>>")

#     if '_' not in my_list:
#         game_over = True
#         print("<<<<<You Win....>>>>>")

#     # print(HangMan_stages.hangman_stages[chances])
