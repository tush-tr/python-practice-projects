# Game - Snake, Water, Gum
# snake + water = snake
# snake + snake = same
# snake + gun = gun
# water + water = same
# water + snake = snake
# water + gun = water
# gun +water = water
# gun+snake=gun
#gun+gun = same
import random
take = input("enter w for Water, s for  Snake and g for Gun?")
c = random.choice(["w","s","g"])
s = f"{take} and {c}"
if s=="s and w":
    print("Snake:: You Win")
elif s=="s and s":
    print("Sorry both are same")
elif s=="s and g":
    print("Gun:: You lose")
elif s=="w and w":
    print("Sorry: both are same")
elif s=="w and s":
    print("Snake: You lose")
elif s=="w and g":
    print("Water:: You Win")
elif s=="g and w":
    print("Water:: You lose")
elif s=="g and s":
    print("Gun:: You win")
elif s=="g and g":
    print("Sorry: Both are same")