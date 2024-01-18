## creating the display function
game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

## creating choice function
def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("Pick position (0,1,2): ")

        if choice not in ['0','1','2']:
            print("Sorry invalid choice! ")
    
    return int(choice)

## choosing a replacement value
