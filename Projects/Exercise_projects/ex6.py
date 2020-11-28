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
# this is simple method of making this program
import random
take = input("enter w for Water, s for  Snake and g for Gun?")
c = random.choice(["Water","Snake","Gun"])
if take=="s" and c=="Water":
    print("Snake:: You Win")
elif take=="s" and c=="Snake":
    print("Sorry both are same")
elif take=="s" and c=="Gun":
    print("Gun:: You lose")
elif take=="w" and c=="Water":
    print("Sorry: both are same")
elif take=="w" and c=="Snake":
    print("Snake: You lose")
elif take=="w" and c=="Gun":
    print("Water:: You Win")
elif take=="g" and c=="Water":
    print("Water:: You lose")
elif take=="g" and c=="Snake":
    print("Gun:: You win")
elif take=="g" and c=="Gun":
    print("Sorry: BOth are same")
