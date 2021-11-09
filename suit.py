import random

user_win = 0
computer_win = 0

option = ['batu', 'gunting', 'kertas']

while True:
    user_input = input('Batu/Gunting/Kertas or Q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in option:
        continue

    rand = random.randint(0,2)
    computer_pick = option[rand]
    print('Computer Pick: ',computer_pick)

    if user_input == 'batu' and computer_pick == 'gunting':
        print('Win')
        user_win += 1
    elif user_input == 'gunting' and computer_pick == 'kertas':
        print('Win')
        user_win += 1
    elif user_input == 'kertas' and computer_pick == 'batu':
        print('Win')
        user_win += 1
    else:
        print('Lose')
        computer_win += 1
print('You win: ',user_win, ' times')
print('Computer Win: ',computer_win, ' times')
print('Goodbye')