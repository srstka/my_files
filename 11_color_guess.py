import random
colors = ["white","red","black","green","brown","blue","yellow","orange","purple"]

print(colors)

right_color = random.choice(colors)

print("******************************")
print("\n")
print("This is a color quessing game!")
print("Can you guess the right color?")
print("\n")
print("******************************")

while True:
    guess = input("What color do i think of? Insert here: ")
    if guess == right_color:
        play_again = input("Do you wanna play again? Type Yes/No: ")
        if play_again == "Yes":
            guess = input("What color do i think of? Insert here: ")
        else:
            break
            
        
    

