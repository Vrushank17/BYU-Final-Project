import random
class Tic_Tac_Toe:
    def __init__(self):
        print("Initialized")
    def drawBoard(self, board):
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
            print("Do you want to be X or O?")
            letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['0', 'X']
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
        return ((bo[1] == le and bo[2] == le and bo[3] == le) or # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
                (bo[7] == le and bo[8] == le and bo[9] == le) or # across the bottom
                (bo[1] == le and bo[4] == le and bo[7] == le) or # down the left side
                (bo[2] == le and bo[5] == le and bo[8] == le) or # down the middle
                (bo[3] == le and bo[6] == le and bo[9] == le) or # down the right side
                (bo[1] == le and bo[5] == le and bo[9] == le) or # diagonal
                (bo[3] == le and bo[5] == le and bo[7] == le)) # diagonal
    
    def isSpaceFree(self, board, move):
        return board[move] == ' '
    def isBoardFull(self, board):
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True
    def Two_Player_Game(self):
        while True:
            theBoard = [''] * 10
            player1Letter,  player2letter = self.inputPlayerLetter()
            turn = self.whoGoesFirst()
            print('The' + turn + 'will go  first.')
            gameIsPlaying = True
            
            while gameIsPlaying:
                if turn == 'player':
                    self.drawBoard(theBoard)
                    move = self.getComputerMove(theBoard, computerLetter)
                    self.makeMove()
game = Tic_Tac_Toe()
game.Two_Player_Game()
