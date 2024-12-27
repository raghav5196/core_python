import random


def play():
    user = input("what is your choice? , 'R' for rock' ,'P' for paper , 'S' for scissors = ")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return 'it\'s a tie'

        r > s, s > p, p > r
    if is_user(user, computer):
        return 'you won!'
    return 'you lost!'


def is_user(player, opponent):
    if (player == 'R' and opponent == 'S') \
            or (player == 'S' and opponent == 'p') \
            or (player == 'P' and opponent == 'R'):
        return True
    return False


print(play())
