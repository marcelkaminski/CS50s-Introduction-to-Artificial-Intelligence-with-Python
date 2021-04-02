"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    flat_list = [item for sublist in board for item in sublist]
    numX = flat_list.count(X)
    numO = flat_list.count(O)

    if numX > numO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                moves.add((row, col))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for mark in [X, O]:

        #horizontally
        for row in range(0, 3):
            if all(board[row][col]==mark for col in range(0, 3)):
                return mark

        #vertically
        for col in range(0, 3):
            if all(board[row][col]==mark for row in range(0, 3)):
                return mark

        #diagonally
        diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for diagonal in diagonals:
            if all(board[row][col]==mark for (row, col) in diagonal):
                return mark

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    flat_list = [item for sublist in board for item in sublist]
    if EMPTY not in flat_list:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    if player(board) == X:
        best_v = -math.inf
        for move in actions(board):
            max_v = min_value(result(board, move))
            if max_v > best_v:
                best_v = max_v
                best_move = move
    
    elif player(board) == O:
        best_v = math.inf
        for move in actions(board):
            min_v = max_value(result(board, move)) 
            if min_v < best_v:
                best_v = min_v
                best_move = move
    return best_move 


def min_value(board):
    """
    Returns the minimum utility of the current board.
    """

    if terminal(board):
        return utility(board)
    
    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v


def max_value(board):
    """
    Returns the maximum utility of the current board.
    """

    if terminal(board):
        return utility(board)

    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v