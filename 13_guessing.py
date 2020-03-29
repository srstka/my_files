import requests
import json
import random
import html 

print("***********************")
print("Welcome to a quiz game!")
print("***********************")
game = input("Do you wanna play? Press 'Enter' to start or type 'quit' to exit the game!").lower()
print("\n")

rounds = 0
score = 0

while game != "quit":
    a = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
    question = json.loads(a.text)
    print(html.unescape(question['results'][0]["question"]))
    options = []
    options.append(question['results'][0]['correct_answer'])
    options.append(question['results'][0]['incorrect_answers'][0])
    options.append(question['results'][0]['incorrect_answers'][1])
    options.append(question['results'][0]['incorrect_answers'][2])
    random.shuffle(options)
    print("The options are: ")
    print("a)", options[0])
    print("b)", options[1])
    print("c)", options[2])
    print("d)", options[3])
    answer = input("What is your answer: ")
    if answer == question['results'][0]['correct_answer']:
        print("Yes your answer was correct! It was ",question['results'][0]['correct_answer'])
        rounds+=1
        score+=1
    else:
        print("Your enswer was wrong! The correct answer was",question['results'][0]['correct_answer'])
        rounds+=1
    print("Your total score is:", score)
    game = input("Do you wanna play? Type 'Yes' to start or 'quit' to exit the game!").lower()
    

print("Game over!")




