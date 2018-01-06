import random
print("IMPORTANT!!! Use space to separate names.       pls")
users_names = input("Enter the names you want to generate a story for:").split(" ")

stories = [
    " became king of Staslomor in 1242 after the death of queen Alexandra.",
    " has won this months lottery! Congrats!",
    " was walking his pet dinosaur in the park one day when suddenly out of nowhere an asteroid struck the park and" +
    " eliminated all life on the planet",
    " lives in a pineapple at the bottom of the ocean and eats sand.",
    " is the a citizen of England, Aether, Roshar, and Zohar.",
    " ate a cookie yesterday.",
    " tried to mount a wild horse and was thrown off. His friends turned him into a meme.",
    " is an octopus who sells sugar free gummy bears for half the price in a shady alleyway.",
    " doesn't exist. Really. No joke."
]

for name in range(len(users_names)):
    rstories = random.choice(stories)
    print(users_names[name] + rstories)
