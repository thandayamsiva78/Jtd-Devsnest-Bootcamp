# options_1="A.TIGER"+"           "+"B.CAT\n""C.KONG"+"            "+"D.ELEPHANT"
# options_2="A.GANGA"+"           "+"B.NILE\n""C.KAVERI"+"          "+"D.INDUS"
# options_3="A.SAHARA"+"          "+"B.GREAT BASIN\n""C.ARABIAN"+"         "+"D.GOBI"
# options_4="A.BENGALURU"+"       "+"B.KOHIMA\n""C.NEW DELHI"+"       "+"D.MUMBAI"

# ######### MEELO YEVARU KOTEESWARULU ##########
# que_1=["a","b","c","d"] # d
# que_2=["a","b","c","d"] # b
# que_3=["a","b","c","d"] # a
# que_4=["a","b","c","d"] # c
# question_1="Which is the largest animal on land?" # Elephant
# question_2="What is the longest river in the world?" # The Nile
# question_3="which desert is the largest  in the word?" # Sahara Desert
# question_4= "What is the capital of India?" # new Delhi
# amount=0
# quit = "quit"

# print("                       let's start the game\n                    WHO WANT TO BE A MILLIONAIRE" )
# name=input("Enrol Your Name:")
# print(f"let's play {name}")
# while True:
#     print(f"1.{question_1}\n{options_1}")
#     user_ans=input("Select one Option::").lower()
#     if user_ans == que_1[3]:
#         print("Correct answer")
#         amount += 100
#         print(f"Win amount {amount} Rs/- ")
#     else:
#         print("Wrong answer selected\n|||GAME OVER|||")
#         print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
#         break
#     print(f"2.{question_2}\n{options_2}")
#     user_ans = input("Select one Option::").lower()
#     if user_ans == que_2[1]:
#         print("Correct answer")
#         amount += 1400
#         print(f"Win amount {amount} Rs/- ")
#     else:
#         print("Wrong answer selected\n|||GAME OVER|||")
#         print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
#         break
#     print(f"3.{question_3}\n{options_3}")
#     user_ans = input("Select one Option::").lower()
#     if user_ans == que_3[0]:
#         print("Correct answer")
#         amount += 3500
#         print(f"Win amount >>>{amount} Rs/- ")
#     else:
#         print("Wrong answer selected\n|||GAME OVER|||")
#         print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
#         break
#     print(f"4.{question_4}\n{options_4}")
#     user_ans = input("Select one Option::").lower()
#     if user_ans == que_4[2]:
#         print("Correct answer")
#         amount += 5000
#         print(f"Win amount>>> {amount} Rs/- ")

#     else:
#         print("Wrong answer selected\n|||GAME OVER|||")
#         print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
#         break
#     print(f"TOTAL WIN PRIZE {amount} Rs/-  ||||CONGRATULATIONS|||| Mr/Mis {name}")
#     break
# # user_ans = input("Select one Option::").lower()
# if user_ans == quit:
#     print("Game over")
#     print(f"TOTAL WIN PRIZE {amount} Rs/-")





print("GAME RULES & OPTIONS:-\n 1. Right or wrong \n 2. QUIT\n 3. LIFELINE(two wrong ans will be removed)\n NOTE: Only one time use \n 4. Audience pol (Host)")
######### MEELO YEVARU KOTEESWARULU ##########
question_1 = "Which is the largest animal on land?" # Elephant
question_2 = "What is the longest river in the world?" # The Nile
question_3 = "which desert is the largest  in the word?" # Sahara Desert
question_4 = "What is the capital of India?" # new Delhi

ans_1 = ["a","b","c","d"]  # d
ans_2 = ["a","b","c","d"]  # b
ans_3 = ["a","b","c","d"]  # a
ans_4 = ["a","b","c","d"]  # c

options_1 = ["A.TIGER","B.CAT","C.KONG","D.ELEPHANT"]
options_2 = ["A.GANGA","B.NILE","C.KAVERI","D.INDUS"]
options_3 = ["A.SAHARA","B.GREAT BASIN","C.ARABIAN","D.GOBI"]
options_4 = ["A.BENGALURU","B.KOHIMA","C.NEW DELHI","D.MUMBAI"]

output_opn_1 = "    ".join(options_1)
output_opn_2 = "    ".join(options_2)
output_opn_3 = "    ".join(options_3)
output_opn_4 = "    ".join(options_4)

amount=0
quit = "quit"

print("                       let's start the game\n                    WHO WANT TO BE A MILLIONAIRE" )
name = input("Enrol Your Name:")
print(f"let's play {name}")
while True:
#-----------------------------------------------------(1)
    print(f"1.{question_1}\n{output_opn_1}")
    user_ans=input("Select one Option:").lower()
    if user_ans == ans_1[3]: #d
        amount += 1000
        print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
    elif user_ans == quit:
        print("You selected \"QUIT\" OPTION \n|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        break
    elif user_ans == "lifeline":
        options_1.remove("B.CAT")
        options_1.remove("C.KONG")
        print(options_1)
        user_ans = input("Select one Option::").lower()
        if user_ans == ans_1[3]:
            amount += 1000
            print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
        else:
            print("WRONG ANSWER SELECTED ❌")
            print("|||GAME OVER|||")
            print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
            print(":::The Correct answer is option D.ELEPHANT")
            break
    else:
        print("WRONG ANSWER SELECTED ❌")
        print("|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        print(":::The Correct answer is option D.ELEPHANT")
        break
#--------------------------------------------------(2)
    print(f"2.{question_2}\n{output_opn_2}")
    user_ans = input("Select one Option::").lower()
    if user_ans == ans_2[1]:
        amount += 4000
        print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
    elif user_ans == quit:
        print("You selected \"QUIT\" OPTION \n|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        break
    elif user_ans == "lifeline":
        options_2.remove("A.GANGA")
        options_2.remove("C.KAVERI")
        print(options_2)
        user_ans = input("Select one Option::").lower()
        if user_ans == ans_2[1]:
            amount += 4000
            print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
        else:
            print("WRONG ANSWER SELECTED ❌")
            print("|||GAME OVER|||")
            print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
            print(":::The Correct answer is option  B.NILE")
            break
    else:
        print("WRONG ANSWER SELECTED ❌")
        print("|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        print(":::The Correct answer is option B.NILE")
        break
#---------------------------------------------------(3)
    print(f"3.{question_3}\n{output_opn_3}")
    user_ans = input("Select one Option::").lower()
    if user_ans == ans_3[0]:
        amount += 45000
        print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
    elif user_ans == quit:
        print("You selected \"QUIT\" OPTION \n|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        break
    elif user_ans == "lifeline":
        options_3.remove("C.ARABIAN")
        options_3.remove("D.GOBI")
        print(options_3)
        user_ans = input("Select one Option::").lower()
        if user_ans == ans_3[0]:
            amount += 45000
            print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
        else:
            print("WRONG ANSWER SELECTED ❌")
            print("|||GAME OVER|||")
            print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
            print(":::The Correct answer is option A.SAHARA")
            break
    else:
        print("WRONG ANSWER SELECTED ❌")
        print("|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        print(":::The Correct answer is option A.SAHARA")
        break
#----------------------------------------------------(4)
    print(f"4.{question_4}\n{output_opn_4}")
    user_ans = input("Select one Option::").lower()
    if user_ans == ans_4[2]:
        amount += 50000
        print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
    elif user_ans == quit:
        print("You selected \"QUIT\" OPTION \n|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        break
    elif user_ans == "lifeline":
        options_4.remove("A.BENGALURU")
        options_4.remove("B.KOHIMA")
        print(options_4)
        user_ans = input("Select one Option:").lower()
        if user_ans == ans_4[2]:
            amount += 50000
            print(f"CORRECT ANSWER ✔️\nWin amount {amount} Rs/- ")
        else:
            print("WRONG ANSWER SELECTED ❌")
            print("|||GAME OVER|||")
            print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
            print(":::The Correct answer is option C.NEW DELHI")
            break
    else:
        print("WRONG ANSWER SELECTED ❌")
        print("|||GAME OVER|||")
        print(f"TOTAL WIN PRIZE {amount} Rs/- CONGRATS...Mr/Mis {name}")
        print(":::The Correct answer is option C.NEW DELHI")
        break
    print(f"TOTAL WIN PRIZE {amount} Rs/-  ||||CONGRATULATIONS|||| Mr/Mis {name}")
    break