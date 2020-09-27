import numpy as np
from bson import ObjectId
from ..database import get_collection
from ..models.connect_models import Game, GameRequest
from typing import List

ROW = 6
COLUMN = 7


def create_board() -> List[List[int]]:
    board = np.zeros((ROW, COLUMN))
    return board.tolist()


def drop_piece(board, row, col, piece):
    board[row][col] = piece
    return board


def print_board(board):
    print(np.flip(board, 0))


def is_valid_location(board, location):
    return board[ROW - 1][location] == 0


def get_next_open_row(board, location):
    for r in range(ROW):
        if board[r][location] == 0:
            return r


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN - 3):
        for r in range(ROW):
            if board[r][c] == piece and \
                    board[r][c + 1] == piece and \
                    board[r][c + 2] == piece and \
                    board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN):
        for r in range(ROW - 3):
            if board[r][c] == piece and \
                    board[r + 1][c] == piece and \
                    board[r + 2][c] == piece and \
                    board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN - 3):
        for r in range(ROW - 3):
            if board[r][c] == piece and \
                    board[r + 1][c + 1] == piece and \
                    board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN - 3):
        for r in range(3, ROW):
            if board[r][c] == piece and \
                    board[r - 1][c + 1] == piece and \
                    board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True


def create_game() -> GameRequest:
    board = create_board()
    connection = get_collection()
    game = Game(
        board=board,
        game_status="STARTED",
        red_move=list(),
        yellow_move=list(),
        next_move="YELLOW"
    )
    _id = connection.insert_one(vars(game))

    new_game = GameRequest(
        status="Ready",
        game_id=str(_id.inserted_id)
    )
    print_board(board)

    return new_game


def get_game(game_id: str) -> Game:
    collection = get_collection()
    response = collection.find_one({"_id": ObjectId(game_id)})
    return response


def update_game(game_id: str, new_game: dict):
    collection = get_collection()
    response = collection.find_one_and_update({"_id": ObjectId(game_id)}, {"$set": new_game})
    return response


def make_move(game, move: int, game_id: str) -> GameRequest:
    board = game["board"]
    move_response = GameRequest()
    move_response.game_id = game_id
    if is_valid_location(board, move):
        updated_game = dict()
        row = get_next_open_row(board, move)
        if game["next_move"] == "YELLOW":
            board = drop_piece(board, row, move, 1)
            game["yellow_move"].append(move)
            updated_game["yellow_move"] = game["yellow_move"]
            updated_game["next_move"] = "RED"
            if winning_move(board, 1):
                updated_game["game_status"] = "FINISHED"
                updated_game["winner"] = "YELLOW"
                move_response.winner = "YELLOW"
                updated_game["next_move"] = None
        else:
            board = drop_piece(board, row, move, 2)
            game["red_move"].append(move)
            updated_game["red_move"] = game["red_move"]
            updated_game["next_move"] = "YELLOW"
            if winning_move(board, 2):
                updated_game["game_status"] = "FINISHED"
                updated_game["winner"] = "RED"
                updated_game["next_move"] = None

                move_response.winner = "RED"

        updated_game["board"] = board
        update_game(game_id, updated_game)
        print_board(board)
        move_response.game_id = game_id
        move_response.status = "Valid"
        return move_response
    else:
        result = np.where(board == 0)
        if len(result[0]) == 1 and len(result[1] == 1):  # Draw condition if the board is filled and cant find 0
            game_draw = dict()
            game_draw["game_status"] = "DRAW"
            game_draw["winner"] = None
            update_game(game_id, game_draw)

        move_response.game_id = game_id
        move_response.status = "Invalid"
        return move_response
