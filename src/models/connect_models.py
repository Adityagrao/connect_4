from pydantic import BaseModel, Field
from typing import List, Optional


class GameRequest(BaseModel):
    game_id: Optional[str] = Field(None, title="Game ID, use this to interact with the game")
    status: Optional[str] = Field(None, title="'Ready' -> Game Started \n 'Valid' -> Valid Move \n 'Invalid' -> "
                                              "Invalid Move")
    winner: Optional[str] = Field(None, title="Specifies winner for a finished Match")


class Game(BaseModel):
    game_id: Optional[str]
    game_status: Optional[str]
    board: Optional[List[List[int]]]
    red_move: Optional[list]
    yellow_move: Optional[list]
    next_move: Optional[str]
    winner: Optional[str]
