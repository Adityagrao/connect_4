import numpy as np
from fastapi import APIRouter, Query, HTTPException
from ..models.connect_models import GameRequest, Game
from ..services.game import create_game, get_game, make_move

router = APIRouter()


@router.post("/Start", response_model=GameRequest)
def start_new_game():
    """
    Initializes a new game.\n
    Returns: \n
        Game ID : ID to interact with the game.\n
        Status : 'Started' when game is started. 'Valid' when a valid move is made. 'Invalid' when the move is invalid.\n
        Winner : Winner of the game - either RED or YELLOW.\n
    """
    response = create_game()
    return vars(response)


@router.post("/Move", response_model=GameRequest)
def game_move(game_id: str = Query(None, title="Game Id"),
              move: int = Query(None, ge=0, le=6)):
    """

    Args:\n
        game_id: Game Id of the game.\n
        move: Move between 0 to 6\n

    Returns:\n
        Game ID : ID to interact with the game.\n
        Status : 'Started' when game is started. 'Valid' when a valid move is made. 'Invalid' when the move is invalid.\n
        Winner : Winner of the game - either RED or YELLOW.\n

    """
    response = get_game(game_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Game not found")
    if response["game_status"] != "STARTED":
        raise HTTPException(status_code=404, detail="Game Ended, can't make more moves")
    res = make_move(response, move, game_id)
    return res


@router.get("/Game", response_model=Game)
def game(game_id: str):
    """

    Args:\n
        game_id: Game Id of the game.\n

    """
    response = get_game(game_id)
    if response is None:
        raise HTTPException(status_code=404, detail="Game not found")
    response["board"] = np.flip(response["board"], 0).tolist()
    response["game_id"] = game_id
    return response
