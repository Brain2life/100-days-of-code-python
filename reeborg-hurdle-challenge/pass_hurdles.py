"""
Make Reeborg pass the hurdles
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for jump in range(6):
    pass_hurdle()