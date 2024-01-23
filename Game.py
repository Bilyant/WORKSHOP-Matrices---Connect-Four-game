from game_funcs import print_matrix, place_player_choice, is_column_full, check_result

rows, cols = 6, 7
matrix = []
game_won = False
turn = 1
for _ in range(rows):
    matrix.append([0 for n in range(cols)])

print_matrix(matrix)
first_player = input('First player, please enter your name: ')
second_player = input('Second player, please enter your name: ')
players_names = [first_player, second_player]

while not game_won:
    player_turn = 1 if turn % 2 == 1 else 2
    player_name = players_names[player_turn - 1]
    print(f'Player {player_name}, please choose a column: ')
    player_choice = input()
    valid_choice = False
    while not valid_choice:
        if not player_choice.isdigit():
            print('Oops that wasn\'t a number. Please try again: ')
            player_choice = input()
            continue

        choice = int(player_choice)
        if choice < 1 or choice > cols:
            print('Nice try! Please choose a number between 1 - 7: ')
            player_choice = input()
            continue

        is_space_available = is_column_full(mx=matrix, rows=rows, col=choice)
        if not is_space_available:
            print('I\'m afraid this column is full. Please choose another one: ')
            player_choice = input()
            continue

        valid_choice = True

    r, c = place_player_choice(mx=matrix, rows=rows, col=int(player_choice), player_n=player_turn)
    print_matrix(matrix)
    game_won = check_result(mx=matrix,mx_r=rows, mx_c=cols, row=r, col=c - 1, player_n=player_turn)
    if game_won:
        print(f'Congratulations! We have a winner. The winner is Player {player_name}')
        break

    turn += 1
