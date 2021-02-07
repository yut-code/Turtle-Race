# Teresa Yu
# Jan 2021
# Turtle Race
# This program is a single-player game that races two turtles to the finish line. 

import turtle
import random

start_p1 = -200, 100
start_p2 = -200, -100

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(start_p1)

player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(start_p2)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(start_p1)

player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(start_p2)


while True:
  if player_one.pos() >= (300,100):
    print("\n\nPlayer One Wins!")
    False

  elif player_two.pos() >= (300,-100):
    print("\n\nPlayer Two Wins!")
    break

  else:
    player_one_turn = raw_input("\nPress the Enter key to roll the die ")
    die1 = random.randint(1, 6)
    print("You rolled: ")
    print(die1)
    print("Turtle moves: ")
    print(20*die1)
    player_one.fd(20*die1)

    player_two_turn = raw_input("\nPress the Enter key to roll the die ")
    die2 = random.randint(1, 6)
    print("You rolled: ")
    print(die2)
    print("Turtle moves: ")
    print(20*die2)
    player_two.fd(20*die2)

    if player_one.pos() >= (300,100) and player_two.pos() >= (300,-100):
      print("Tie!")
      break
