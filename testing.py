# Just testing straight python here before copying into app.py

from random import randint
def dicegame():
    rolled_number = randint(1, 6)

    if (rolled_number == 6):
        return "You rolled a 6. You won!"
    elif (rolled_number != 6):
        return f'You rolled a {rolled_number}. You lost!'

print(dicegame())
    