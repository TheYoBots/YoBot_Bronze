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
import sys

logger = logging.getLogger(__name__)

def get_best_move(board: chess.Board) -> chess.Move:

    my_color = board.turn
    global_max_score = -sys.maxsize
    best_moves = []

    for my_candidate_move in list(board.legal_moves):

        board.push(my_candidate_move)

        if board.is_checkmate():
            return my_candidate_move

        candidate_min_score = sys.maxsize

        for opponent_candidate_move in list(board.legal_moves):

            board.push(opponent_candidate_move)

            if board.is_checkmate():
                current_score = -9999
            else:
                current_score = __get_board_total_score(board, my_color)

            if current_score < candidate_min_score:
                candidate_min_score = current_score

            board.pop()

        if candidate_min_score > global_max_score:
            global_max_score = candidate_min_score
            best_moves = [my_candidate_move]
        elif candidate_min_score == global_max_score:
            best_moves.append(my_candidate_move)

        board.pop()

    best_move = random.choice(best_moves)

    # Always promote to queen.
    if best_move.uci()[-1].isalpha():
        best_move.promotion = chess.QUEEN

    return best_move

def get_board_score(board: chess.Board, color: chess.Color) -> int:

    total = 0

    pawns = board.pieces(chess.PAWN, color)
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

def __get_board_total_score(board: chess.Board, color: chess.Color) -> int:

    color_score = get_board_score(board, color)
    opposite_color_score = get_board_score(board, not color)
    return color_score - opposite_color_score