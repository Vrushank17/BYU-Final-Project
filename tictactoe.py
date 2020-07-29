import random


class Tic_Tac_Toe:
    def drawBoard(self, board):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')

    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print("Do you want to be X or O?, Player1")
            letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        if random.randint(0, 1) == 0:
            return 'player 1'
        else:
            return 'player 2'

    def playAgain(self):
        print('Do you want to play again?(yes or no)')
        return input().lower().startswith('y')

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[1] == le and bo[2] == le and bo[3] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[7] == le and bo[8] == le and bo[9] == le) or  # across the bottom
                (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the left side
                (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the middle
                (bo[3] == le and bo[6] == le and bo[9] == le) or  # down the right side
                (bo[1] == le and bo[5] == le and bo[9] == le) or  # diagonal
                (bo[3] == le and bo[5] == le and bo[7] == le))  # diagonal

    def isSpaceFree(self, board, move):
        return board[move] == ' '

    def isBoardFull(self, board):
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True

    def makeMove(self, board, letter, move):
        board[move] = letter

    def getBoardCopy(self, board):
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    def getPlayerMove(self, board):
        move = input('Make your move (1-9)')

        while move not in '1 2 3 4 5 6 7 8 9'.split():
            print("Invalid move. Please try again")
            move = input("Make your move")
        
        return int(move)

    def Two_Player_Game(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            theBoard = [' '] * 10
            player1Letter, player2Letter = self.inputPlayerLetter()
            turn = self.whoGoesFirst()
            print(turn + ' will go first')
            gameIsPlaying = True
            while gameIsPlaying:
                if turn == 'player 1':
                    self.drawBoard(theBoard)
                    move = self.getPlayerMove(theBoard)
                    self.makeMove(theBoard, player1Letter, move)
                    if self.isWinner(theBoard, player1Letter):
                        self.drawBoard(theBoard)
                        print("Player One has Won the Game!")
                        break
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('The game is a Tie!')
                            break
                        else:
                            turn = 'player 2'
                # Player Two Turn
                elif turn == 'player 2':
                    self.drawBoard(theBoard)
                    move = self.getPlayerMove(theBoard)
                    self.makeMove(theBoard, player2Letter, move)
                    if self.isWinner(theBoard, player2Letter):
                        self.drawBoard(theBoard)
                        print("Player Two has Won the Game!")
                        break
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('The game is a Tie!')
                            break
                        else:
                            turn = 'player 1'

            print('Do you want to play again? (yes or no)')

            if not input().lower().startswith('y'):
                break




print('''Hello! Welcome to Tic-Tac-Toe. Here is a small picture of the game boardL
            |     |
         1  |  2  |  3
       -----|-----|-----
         4  |  5  |  6
       -----|-----|-----
         7  |  8  |  9
            |     |
        To make your move, type a number between 1 and 9 to place your letter in the corresponding spot as shown in the example. 
        ''')


game = Tic_Tac_Toe()
game.Two_Player_Game()
