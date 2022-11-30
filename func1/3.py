# Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among 
# the chickens and rabbits in a farm.
# How many rabbits and how many chickens
# do we have? create function:
# solve(numheads, numlegs):
import math

def solve(numheads, numlegs):
    x = numlegs / 2 - numheads # num if rabbits
    y = numheads - x # num of chickens
    print("Number of rabbits: ", x)
    print("Number of chickens:", y)

hd = 35 #num if heads
lg = 94 #num of legs
solve(hd, lg)
