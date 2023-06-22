import numpy as np
from tabulate import tabulate

def check_winner(valid_entries: list, playground: np.array):
    '''
    the function checks for winners given the available moves and current playground situation
    input:
        valid_entries: available moves
        playground: tic-tac-toe board with current playground situation
    return
        s (str) - name of the winner or 'Match Drawn!' | None if no winner yet and moves are available.
    '''

    # check for three consecutive identical marker in the inverse diagonal of the matrix
    inverse_diagonal_values = np.flipud(playground).diagonal().tolist()
    if len(set(inverse_diagonal_values)) == 1 and set(inverse_diagonal_values) != {''}:
        print(f"\nWhohoooooooo! We have a Winner! It's Player {inverse_diagonal_values[0]}!")
        return inverse_diagonal_values[0]
    
    # check for three consecutive identical marker in the diagonal of the matrix
    diagonal_values = playground.diagonal().tolist()
    if len(set(diagonal_values)) == 1 and set(diagonal_values) != {''}:
        print(f"\nWhohoooooooo! We have a Winner! It's Player {diagonal_values[0]}!")
        return diagonal_values[0]

    # check for three consecutive identical marker in all the rows and columns of the matrix
    for i in range(2):
        col_values = playground[:, i].tolist()
        row_values = playground[i, :].tolist()

        # for column
        if len(set(col_values)) == 1 and set(col_values) != {''}:
            print(f"\nWhohoooooooo! We have a Winner! It's Player {col_values[0]}!")
            return col_values[0]

        # for row
        if len(set(row_values)) == 1 and set(row_values) != {''}:
            print(f"\nWhohoooooooo! We have a Winner! It's Player {row_values[0]}!")
            return row_values[0]

    # if no winner yet, then checking the number of available moves. if 0, it means match is drawn.
    if valid_entries == []:
        print(f"\n Uh-Oh! Both the players are equally good at Tic-Tac-Toe! Match Drawn!")
        return 'Match Drawn!'
    
    return None


def player_turn(player_marker: str, valid_entries: list, playground: np.array):
    '''
    the function takes user input for the position the player want to mark and updates necessary variables and checks for the winner.
    input:
        player_marker: marker for player whose turn it is.
        valid_entries: available moves
        playground: tic-tac-toe board with current playground situation
    return:
        valid_entries (list): updates available moves
        playground (np.array): updated tic-tac-toe board
        winner (str): winner, if any, with the latest move
    '''
    while True:
        p = str(input(f'Player {player_marker}, enter a value from {valid_entries}'))
        if p in valid_entries:
            valid_entries.remove(p)
            playground[int(p[0])][int(p[1])] = player_marker
            break
        else:
            print('Invalid Value Entered! Try Again!')

    print(f'Playground after Player {player_marker} move - ')
    print(tabulate(playground, tablefmt='grid'))
    
    winner = check_winner(valid_entries=valid_entries, playground=playground)

    return valid_entries, playground, winner

if __name__ == '__main__':

    player1_marker = 'X' # marker for the player with first chance
    player2_marker = 'O' # marker for the player with second chance
    playground = np.array([['', '', ''], ['', '', ''], ['', '', '']]) # empty tic-tac-toe board
    valid_entries = ['00', '01', '02', '10', '11', '12', '20', '21', '22'] # available and valid moves

    while True:
        
        # player x turn
        valid_entries, playground, winner = player_turn(player_marker=player1_marker, valid_entries=valid_entries, playground=playground)
        if winner:
            break
        
        # player o turn
        valid_entries, playground, winner = player_turn(player_marker=player2_marker, valid_entries=valid_entries, playground=playground)
        if winner:
            break