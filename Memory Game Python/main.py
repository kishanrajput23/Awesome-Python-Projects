import random
import os

values = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
table_heading = {65:"A", 66:"B", 67:"C", 68:"D", 69:"E", 70:"F", 71:"G", 72:"H"}
temp_found = []
user_values = []
user_choices = []
progress = True
competed = False

user_choice_data = input("""
For '2x2' enter "EASY"
For '4x4' enter "MEDIUM"
For '6x6' enter "HARD"
For '8x8' enter "EXTREME"

Enter your choice: """).lower()

while user_choice_data not in ["easy", "medium", "hard", "extreme"]:
    os.system("cls")
    user_choice_data = input("""
For '2x2' enter "EASY"
For '4x4' enter "MEDIUM"
For '6x6' enter "HARD"
For '8x8' enter "EXTREME"

Enter your choice: """).lower()

def game_elements(num):
    
    lst = []
    while len(lst) < num:
        row = []
        while len(row) < num:
            random_number = random.randint(1,10)
            if random_number not in row:
                row.append(random_number)
        lst.append(row)
        element = row.copy()
        random.shuffle(element)
        lst.append(element)
    return lst

def game_process(num):
    global user_values
    global temp_found
    global competed

    def game_table(list_with_spaces):
        char_count = 65
        if user_choice_data == 2:
            print("        0         1     ")
            print("   |---------|---------|")
            for i in range(2):
                print(f"{table_heading[char_count]}  |    {list_with_spaces[i][0]}    |    {list_with_spaces[i][1]}    |")
                print("   |---------|---------|")
                char_count += 1

        if user_choice_data == 4:
                print("        0         1         2         3     ")
                print("   |---------|---------|---------|---------|")
                for i in range(4):
                    print(f"{table_heading[char_count]}  |    {list_with_spaces[i][0]}    |    {list_with_spaces[i][1]}    |    {list_with_spaces[i][2]}    |    {list_with_spaces[i][3]}    |")
                    print("   |---------|---------|---------|---------|")
                    char_count += 1

        
        if user_choice_data == 6:
                print("       0       1       2       3       4       5    ")
                print("   |-------|-------|-------|-------|-------|-------|")
                for i in range(6):
                    print(f"{table_heading[char_count]}  |   {list_with_spaces[i][0]}   |   {list_with_spaces[i][1]}   |   {list_with_spaces[i][2]}   |   {list_with_spaces[i][3]}   |   {list_with_spaces[i][4]}   |   {list_with_spaces[i][5]}   |")
                    print("   |-------|-------|-------|-------|-------|-------|")
                    char_count += 1

        
        if user_choice_data == 8:
                print("       0       1       2       3       4       5       6       7    ")
                print("   |-------|-------|-------|-------|-------|-------|-------|-------|")
                for i in range(8):
                    print(f"{table_heading[char_count]}  |   {list_with_spaces[i][0]}   |   {list_with_spaces[i][1]}   |   {list_with_spaces[i][2]}   |   {list_with_spaces[i][3]}   |   {list_with_spaces[i][4]}   |   {list_with_spaces[i][5]}   |   {list_with_spaces[i][6]}   |   {list_with_spaces[i][7]}   |")
                    print("   |-------|-------|-------|-------|-------|-------|-------|-------|")
                    char_count += 1


    list_with_spaces = [[' ' for _ in sublist] for sublist in main]
    while progress:
        os.system('cls')
        game_table(list_with_spaces)
        
        trial = 0
        for i in range(2):
            if len(user_choices) == (num**2):
                competed = True
                break

            opn = input("\nEnter the tile to uncover: ")
            while opn in user_choices:
                print("\n===========>>>You have already completed this tile!")
                opn = input("\nEnter the new tile to uncover: ")
            user_values.append(opn)

            index_1 = values[opn[0]]
            index_2 = int(opn[1])

            temp_found.append(main[index_1][index_2])
            
            list_with_spaces[index_1][index_2] = main[index_1][index_2]
            game_table(list_with_spaces)
            
            trial += 1
            if trial == 2:
                user_input = input("\n===========>>> Press (Enter) to Continue: ")
                trial = 0

        if competed:
            print("\n===========>>> You Won! <<<===========")
            break
        elif temp_found[0] == temp_found[1]:
            for i in range(2):
                user_choices.append(user_values[i])
                index_1 = values[user_values[i][0]]
                index_2 = int(user_values[i][1])
                list_with_spaces[index_1][index_2] = "✔️" 
            user_values = []
            temp_found = []
        else:
            for i in range(2):
                index_1 = values[user_values[i][0]]
                index_2 = int(user_values[i][1])
                list_with_spaces[index_1][index_2] = " "
            user_values = []
            temp_found = []
while True:
    if user_choice_data == "easy":
        user_choice_data = 2
    if user_choice_data == "medium":
        user_choice_data = 4
    if user_choice_data == "hard":
        user_choice_data = 6
    if user_choice_data == "extreme":
        user_choice_data = 8
    main = game_elements(user_choice_data)
    process = game_process(user_choice_data)

    choice = input("Do you want to play the game again? (y/n): ").lower()

    while choice not in ["y", "n"]:
        print("\n Invalid choice")
        choice = input("Do you want to play the game again? (y/n): ")
    
    if choice == "n":
        break