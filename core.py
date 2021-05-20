# This file is part of YoBot_Bronze UCI Chess Engine.
# Copyright (C) 2021- Yohaan Seth Nathan (TheYoBots)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# You should have received a copy of the MIT License along with this 
# UCI Chess Engine. If not, view this https://opensource.org/licenses/MIT

import logging
import chess
import random

logger = logging.getLogger(__name__)

def getBestMove(board: chess.Board) -> chess.Move:

    for candidate_move in list(board.legal_moves):

        board.push(candidate_move)
        if board.is_checkmate():
            logging.info(f"{candidate_move} will checkmate, this is the best move")
            return candidate_move
        else:
            board.pop()


    return random.choice(list(board.legal_moves))