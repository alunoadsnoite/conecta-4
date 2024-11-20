import numpy as np

NAME = "Valdenor"

# Parâmetros de colônia de abelhas ajustados para eficiência
NUM_BEES_START = 10       # Menos abelhas no início para velocidade
NUM_BEES_END = 20         # Mais abelhas nas últimas jogadas para precisão
DEPTH_START = 2           # Profundidade menor no início
DEPTH_END = 3             # Profundidade maior nas jogadas finais
EXPLORE_FACTOR = 0.5      # Fator de exploração moderado para estabilidade

def jogada(board, piece):
    # Ajusta parâmetros conforme o tabuleiro está preenchido
    filled_cols = np.count_nonzero(board[0])  # Conta as colunas parcialmente preenchidas
    num_bees = NUM_BEES_END if filled_cols > 30 else NUM_BEES_START
    depth = DEPTH_END if filled_cols > 30 else DEPTH_START

    # Executa a busca usando o modelo ajustado
    scores = bee_swarm_search(board, piece, num_bees, depth)
    best_col = np.argmax(scores)  # Escolhe a coluna com maior pontuação
    return best_col

def bee_swarm_search(board, piece, num_bees, depth):
    scores = np.zeros(7)
    for col in range(7):
        if is_valid_location(board, col):
            bee_scores = []

            # Simulação com o número de abelhas ajustado
            for _ in range(num_bees):
                simulated_board = board.copy()
                row = get_next_open_row(simulated_board, col)
                drop_piece(simulated_board, row, col, piece)
                bee_scores.append(simulate_path(simulated_board, piece, depth))
            
            # Média ponderada das pontuações com fator de exploração
            scores[col] = np.mean(bee_scores) * EXPLORE_FACTOR
    return scores

def simulate_path(board, piece, depth):
    if depth == 0 or is_terminal_node(board):
        return score_position(board, piece)
    
    valid_locations = [c for c in range(7) if is_valid_location(board, c)]
    scores = []
    
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        next_piece = 1 if piece == 2 else 2
        score = simulate_path(temp_board, next_piece, depth - 1)
        scores.append(score)

    return max(scores) if piece == 2 else min(scores)

# Funções auxiliares
def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_terminal_node(board):
    return winning_move(board, 1) or winning_move(board, 2) or all(not is_valid_location(board, c) for c in range(7))

def winning_move(board, piece):
    for row in range(6):
        for col in range(4):
            if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
                return True
    for col in range(7):
        for row in range(3):
            if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and board[row + 3][col] == piece:
                return True
    for row in range(3):
        for col in range(4):
            if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
                return True
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                return True
    return False

def score_position(board, piece):
    # Avaliação simplificada priorizando o centro para eficiência
    score = 0
    center_array = [int(i) for i in list(board[:, 3])]
    center_count = center_array.count(piece)
    score += center_count * 3
    return score
