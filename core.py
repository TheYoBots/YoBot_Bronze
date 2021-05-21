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

    checkMateMove = getCheckMateMove(board)

    if checkMateMove != None:
        return checkMateMove

    opponent_color = not board.turn

    opponent_initial_score = getBoardScore(board, opponent_color)
    min_opponent_score = opponent_initial_score

    best_move = None

    for candidate_move in list(board.legal_moves):
        board.push(candidate_move)
        candidate_move_score = getBoardScore(board, opponent_color)
        if candidate_move_score < min_opponent_score and candidate_move_score < opponent_initial_score:
            min_opponent_score = candidate_move_score
            best_move = candidate_move
        board.pop()

    if best_move == None:
        return random.choice(list(board.legal_moves))
    else:
        return best_move

def getBoardScore(board: chess.Board, color: chess.Color) -> int:

    total = 0

    pawns =  board.pieces(chess.PAWN, color)
    bishops = board.pieces(chess.BISHOP, color)
    knights = board.pieces(chess.KNIGHT, color)
    queens = board.pieces(chess.QUEEN, color)
    rooks = board.pieces(chess.ROOK, color)

    for pawn in pawns:
        total = total + 1 
    for bishop in bishops:
        total = total + 3
    for knight in knights:
        total = total + 3
    for queen in queens:
        total = total + 9
    for rook in rooks:
        total = total + 5

    return total

def getCheckMateMove(board: chess.Board) -> chess.Move:

    for candidate_move in list(board.legal_moves):

        board.push(candidate_move)
        if board.is_checkmate():
            logging.info(f"{candidate_move} is my best move")
            return candidate_move
        else:
            board.pop()


    return None