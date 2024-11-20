import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import jogador_random as p1 # Importa o módulo do jogador
import valdenor as p2

# Configurações do tabuleiro
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

def is_valid_location(board, col):
    return board[ROWS - 1][col] == EMPTY

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

def print_board(board):
    print(np.flip(board, 0))

def check_win(board, piece):
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True, [(r, c), (r, c + 1), (r, c + 2), (r, c + 3)]

    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True, [(r, c), (r + 1, c), (r + 2, c), (r + 3, c)]

    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True, [(r, c), (r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)]

    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True, [(r, c), (r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3)]

    return False, []  # Retorna False e lista vazia se não houver vitória

def draw_board(board, winning_moves=None):
    plt.clf()
    plt.title("Conecta 4")
    plt.xlim(0, COLS)
    plt.ylim(0, ROWS)
    plt.xticks(np.arange(COLS))
    plt.yticks(np.arange(ROWS))
    plt.grid()

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == PLAYER1:
                color = 'red'
            elif board[r][c] == PLAYER2:
                color = 'yellow'
            else:
                color = 'lightgrey'

            rect = Rectangle((c, r), 1, 1, color=color, edgecolor='black', linewidth=2)
            plt.gca().add_patch(rect)

            if winning_moves and (r, c) in winning_moves:
                rect.set_edgecolor('black')
                rect.set_linewidth = 6
    # Adiciona a legenda com os nomes dos jogadores
    plt.legend(
        [Rectangle((0, 0), 1, 1, color='red', edgecolor='black'),
         Rectangle((0, 0), 1, 1, color='yellow', edgecolor='black')],
        [p1.NAME, p2.NAME],
        loc='upper left',
        bbox_to_anchor=(0, 0)  # Ajusta a posição da legenda
    )

    plt.pause(0.5)

def show_result(message):
    plt.text(3.5, 3, message, fontsize=15, ha='center', va='center', color='black', fontweight='bold')
    plt.pause(5)

def game_loop():
    board = create_board()
    game_over = False
    turn = np.random.randint(0, 2) #faz com que o jogo possa começar pelo jogador 1 ou 2 aleatoriamente

    while not game_over:
        draw_board(board)
        current_player = PLAYER1 if turn % 2 == 0 else PLAYER2
        current_player_name=""

        if current_player == PLAYER1:
            col = p1.jogada(board, current_player)  # Função do jogador 1
            current_player_name=p1.NAME;
        else:
            col = p2.jogada(board, current_player)  # Função do jogador 2
            current_player_name=p2.NAME;

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, current_player)

            win, winning_moves = check_win(board, current_player)
            if win:
                draw_board(board, winning_moves)
                show_result(f"Jogador {current_player_name} venceu!")
                game_over = True
        else:
            draw_board(board)
            show_result(f"Jogada inválida!\n Jogador {current_player_name} cometeu uma infração \ne perdeu o jogo.")
            game_over = True

        turn += 1


if __name__ == "__main__":
    plt.ion()
    game_loop()
    plt.ioff()
    plt.show()
