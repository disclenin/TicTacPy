class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']
        self.current_player = self.players[0]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play(self):
        print("Добро пожаловать в игру 'Крестики-нолики'!")

        while True:
            self.print_board()

            if self.current_player == 'X':
                row = int(input("Введите номер строки (0, 1, 2): "))
                col = int(input("Введите номер столбца (0, 1, 2): "))
            else:
                row, col = self.minimax()

            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.print_board()
                    print(f"Игрок {self.current_player} победил!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("Ничья!")
                    break
                else:
                    self.switch_player()
            else:
                print("Эта ячейка уже занята. Попробуйте еще раз.")

    def minimax(self):
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax_helper(0, False)
                    self.board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def minimax_helper(self, depth, is_maximizing):
        scores = {'X': -1, 'O': 1, 'tie': 0}

        if self.check_winner('X'):
            return scores['X'] - depth
        elif self.check_winner('O'):
            return scores['O'] + depth
        elif self.is_board_full():
            return scores['tie']

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax_helper(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax_helper(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
