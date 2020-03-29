import time
import matplotlib.pyplot as plt
import random

words = ["house","princes","spiderman","pocahontas","aquaman"]

word = random.choice(words)

x = [1,2,3,4,5]
y = []
errors = 0

print("Type this word five times: ",word)

for i in range(0,5):
    a = time.time()
    word2 = input("Type the word now: ")
    b = time.time()
    y.append(b-a)
    if word2 != word:
        errors+=1

print("You have made so many errors: ",errors)

legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing propgres")

plt.plot(x,y)
plt.show()


