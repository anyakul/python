# 39) Создайте программу для игры в "Крестики-нолики".


from random import randint


X = 'X'
O = '0'
MODE_1 = 'computer'
MODE_2 = 'person'


def show_field(nums):
    cell = 1

    for i in range(0, 3):
        for j in range(0, 3):
            print(nums[cell], end=' ')
            cell += 1
        print(' ')


def get_win(nums):
    if (nums[1] == nums[2] == nums[3]) or \
        (nums[4] == nums[5] == nums[6]) or \
        (nums[7] == nums[8] == nums[9]) or \
        (nums[1] == nums[4] == nums[7]) or \
        (nums[2] == nums[5] == nums[8]) or \
        (nums[3] == nums[6] == nums[9]) or \
        (nums[1] == nums[5] == nums[9]) or \
            (nums[3] == nums[5] == nums[7]):
        return True
    else:
        return False


def check_input(nums, num):
    if num < 1 or num > 9 or (nums[num] == X) or (nums[num] == O):
        return False
    else:
        return True


def computer_move(nums):
    num = randint(1, 9)
    check_input(nums, num)
    while check_input(nums, num) == False:
        num = randint(1, 9)
        check_input(nums, num)

    return num


def player_move(nums, move):
    num = int(input(f'Введите незанятое число от 1 до 9 за {move}: '))
    check_input(nums, num)
    while check_input(nums, num) == False:
        num = int(input(f'Введите незанятое число от 1 до 9 за {move}: '))
        check_input(nums, num)

    return num


def do_move(move, num):
    if move == X:
        nums[num] = X
        if get_win(nums) == True:
            print(f'Выиграли {move}')
            move = 'finish'
        else:
            move = O
    elif move == O:
        nums[num] = O
        if get_win(nums) == True:
            print(f'Выиграли {move}')
            move = 'finish'
        else:
            move = X

    return move


def play_game(nums, mode, players_move='no'):
    num = 0
    move = X
    count_move = 0
    get_win(nums)

    while get_win(nums) == False or count_move == 9:
        if mode == 'person':
            num = 0
            num = player_move(nums, move)
            move = do_move(move, num)
            count_move += 1
            if move == 'finish' and count_move <= 9:
                break
            elif move != 'finish' and count_move == 9:
                print('Ничья')
                break
        elif mode == 'computer':
            if move != players_move and move != 'finish' and count_move != 9:
                num = 0
                num = computer_move(nums)
                move = do_move(move, num)
                count_move += 1
                show_field(nums)
            elif move == players_move and move != 'finish' and count_move != 9:
                num = 0
                num = player_move(nums, move)
                move = do_move(move, num)
                count_move += 1
                show_field(nums)
            elif move == 'finish' and count_move <= 9:
                break
            elif move != 'finish' and count_move == 9:
                print('Ничья')
                break


nums = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

show_field(nums)
mode_num = int(input('Выберите режим (1 - с компьютером, 2 - с человеком): '))

if mode_num == 1:
    mode = MODE_1
if mode_num == 2:
    mode = MODE_2
    move = 'no'

if mode_num == 1:
    move_choose = input(
        'Выберите за кого будете играть (x или 0), x ходят первыми: ')
    if move_choose == 'x':
        move = X
    elif move_choose == '0':
        move = O

play_game(nums, mode, move)
