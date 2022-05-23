# importing installed library
import pyjokes, random
  
My_jokes = pyjokes.get_jokes(language="en", category="all")
random.shuffle(My_jokes)

numJokes = int(input("How many jokes do you want me to tell?"
                     "(enter a whole number please):"))

print("Here are your " + str(numJokes) + " jokes:\n")
for i in range(0, numJokes):
    print(My_jokes[i] + ' \n')
