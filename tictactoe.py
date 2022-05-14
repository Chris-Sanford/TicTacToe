def display_board(board): #Defines display_board function
    #Accepts one parameter containing the board's current status and prints it out to the console

    #Sets a variable to a visual representation of the current status of the board, {} representing the value at a particular index as indicated in .format()
    boardDisplay = """
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    """.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2])

    print(boardDisplay) #Prints the visual of the current board status

def enter_move(board): #Defines enter_move function
    #Accepts the board's current status, asks the user what their next move is, checks the input, and updates the board according to the user's decision

    while True: #This will engage an infinite loop until we hit a break
        try: #Try to get a valid integer input without running into an error
            selectedField = int(input("Enter the number of a space you'd like to place your O on: ")) #Prompt user to input their next move
        except: #If Python throws an error/exception when trying to convert the input to an integer:
            print("You must input an integer, not a string (words) or float number with decimals (1.01).")
            continue #Start the loop from the beginning
        if type (selectedField) == int and selectedField > 0 and selectedField < 10 and selectedField in make_list_of_free_fields(board): #If the input meets all conditions that make for a legit move
            for i in range(3): #For each space in the board's 3 rows
                for j in range(3): #For each space in the board's 3 columns
                    if board[i][j] == selectedField: #If the currently-iterated field matches the selectedField
                        board[i][j] = "O" #Set the currently-iterated field to "O" representing the user's move
            break
        else:
            print("You did not enter a valid input for a free space. Try again.")
            continue #Start the loop from the beginning

def make_list_of_free_fields(board): #Defines the make_list_of_free_fields function
    #Parses the board and builds a list of all the free squares
    
    freeFields = [] #Reset freeFields variable

    for i in range(3): #For each space in the board's 3 rows
        for j in range(3): #For each space in the board's 3 columns
            if board[i][j] != "X" and board[i][j] != "O": #If the currently-iterated field is not an X or an O, it is not occupied, and therefore free
                freeFields.append(board[i][j]) #Appends the currently-iterated field that has been verified to be free

    return freeFields #This will return freeFields when the function is called, enabling enter_move() to use the freeFields list

def victory_for(board): #Checks to see if someone has won
    #Analyzes the board's status in order to check if the player using 'O's or 'X's has won the game

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": #if horizontal1 is all Xs:
        result = "computer"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X": #horizontal2
        result = "computer"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X": #horizontal3
        result = "computer"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X": #vertical1
        result = "computer"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X": #vertical2
        result = "computer"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X": #veritcal3
        result = "computer"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": #diagonal1
        result = "computer"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": #diagonal2
        result = "computer"
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O": #if horizontal1 is all Os:
        result = "user"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O": #horizontal2
        result = "user"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O": #horizontal3
        result = "user"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O": #vertical1
        result = "user"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O": #vertical2
        result = "user"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O": #veritcal3
        result = "user"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": #diagonal1
        result = "user"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": #diagonal2
        result = "user"
    else:
        intExists = False #Set intExists to False by default

        #Check to see if the game is over by looping through all rows and columns looking for an integer (free field)
        for row in range(3): #For each space in the board's 3 rows
            for column in range(3): #For each space in the board's 3 columns
                if type(board[row][column]) == int: #Check if currently iterated field is an integer (meaning it's a free space)
                    intExists = True #If it's an int, set intExists to True
                    break #Once we've found an int, no need to keep looking

        if intExists == True: #If there is an int (free space left on the board)
            result = "null" #There is no result, the game continues
        elif intExists == False: #If there are no ints (no free spaces left)
            result = "draw" #There are no free spaces left, the game is over. Since we already checked for all possible win conditions, it's a draw.

    #Output the results to the console
    if result == "computer" or result == "user":
        print("The",result,"player won!")
        return True
    elif result == "draw":
        print("The game ended in a draw.")
        return True
    elif result == "null":
        return False

def draw_move(board): #Defines draw_move function
    #Prompts computer to make its next move

    from random import randrange #Import randrange to select a random number within the range of free fields

    selectedIndex = randrange(len(make_list_of_free_fields(board))) #Select a random index within freeFields

    computerMove = make_list_of_free_fields(board)[selectedIndex] #Get the value from the freeFields index

    #Loop through all rows and columns looking for the computer's desired field
    for row in range(3): #For each space in the board's 3 rows
        for column in range(3): #For each space in the board's 3 columns
            if board[row][column] == computerMove: #Check if currently iterated field is the computer's choice
                board[row][column] = "X" #Set the field to X
                break #Once we've found the index value we were looking for, stop looping

#Defining variables outside of a function because otherwise the variables are not global and cannot be passed into other functions
board = [[1,2,3],[4,5,6],[7,8,9]] #Defines the 3-element list board containing 3 different 3-element lists. board contains 3 elements that are lists, those sub-lists contain 3 elements that are integers representing free spaces
board[1][1] = "X" #Sets middle free space (5) to computer's first move

while victory_for(board) is False: #Check to see if either player has won yet
    display_board(board) #Show the current state of the board
    make_list_of_free_fields(board) #Determine which spaces are available
    enter_move(board) #Prompt user to enter move
    if victory_for(board) is True: #If the user player won with their last move
        display_board(board) #Show the current state of the board
        break #This will end the while loop, and thus, the game
    make_list_of_free_fields(board) #Re-calculate the free spaces in preparation for computer's next move
    draw_move(board) #Prompt computer to do its next move
    if victory_for(board) is True: #If the computer player won with its last move
        display_board(board) #Show the current state of the board
        break #This will end the while loop, and thus, the game