

from player import HumanPlayer, ComputerPlayer
from game import Game

def main():

    # player1 = HumanPlayer("Игрок 1", "X") #Вариант игры человека в консоли
    player1 = ComputerPlayer("Компьютер 1", "X") #Игрок - компьютер
    player2 = ComputerPlayer("Компьютер 2", "O") #Игрок - компьютер

    game = Game(player1, player2) 

    game.play()

if __name__ == "__main__":
    main()