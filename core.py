import logging
import chess
import random

logger = logging.getLogger(__name__)

board = None

def getBestMove(board: chess.Board) -> chess.Move:

    return random.choice(list(board.legal_moves))