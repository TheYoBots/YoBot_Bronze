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

    #attacked_pieces = get_attacked_pieces(board, my_color)
    #print(attacked_pieces)

    for my_candidate_move in list(board.legal_moves):

        board.push(my_candidate_move)

        if board.is_checkmate():
            return my_candidate_move

        is_my_candidate_move_attacked = __is_attacked(board, my_candidate_move.to_square)

        candidate_min_score = sys.maxsize

        for opponent_candidate_move in list(board.legal_moves):

            board.push(opponent_candidate_move)

            if board.is_checkmate():
                current_score = -9999
            else:
                current_score = __get_board_total_score(board, my_color)
                if is_my_candidate_move_attacked:
                    current_score = current_score + 1

            candidate_min_score = min(current_score, candidate_min_score)

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


def get_attacked_pieces(board: chess.Board, defending_color: chess.Color):

    attacked_pieces = { }

    for square, piece in board.piece_map().items():

        if board.color_at(square) != defending_color:
            continue

        attacking_pieces = get_attacking_pieces(board, not defending_color, square)
        if len(attacking_pieces) > 0:

            defending_pieces = get_defending_pieces(board, defending_color, square)
            attacked_pieces[square] = (piece.piece_type, attacking_pieces, defending_pieces)

    return attacked_pieces

def __is_attacked(board: chess.Board, square: chess.Square):

    return len(board.attacks(square)) > 1

def get_attacking_pieces(board: chess.Board, attacking_color: chess.Color, square: chess.Square) -> [chess.PieceType]:

    piece_types = []

    attacking_squares = board.attackers(attacking_color, square)

    for attacking_square in attacking_squares:

        if board.is_pinned(attacking_color, attacking_square) == False:
            piece_type = board.piece_type_at(attacking_square)
            piece_types.append(piece_type)

    return piece_types

def get_defending_pieces(board: chess.Board, defending_color: chess.Color, square: chess.Square) -> [chess.PieceType]:

    cloned_board = board.copy()

    defending_pieces = get_attacking_pieces(cloned_board, defending_color, square)

    del cloned_board

    return defending_pieces

def get_board_score(board: chess.Board, color: chess.Color) -> int:

    total = 0

    pawns = board.pieces(chess.PAWN, color)
    bishops = board.pieces(chess.BISHOP, color)
    knights = board.pieces(chess.KNIGHT, color)
    queens = board.pieces(chess.QUEEN, color)
    rooks = board.pieces(chess.ROOK, color)

    for _ in pawns:
        total += 10
    for _ in bishops:
        total += 30
    for _ in knights:
        total += 30
    for _ in queens:
        total += 90
    for _ in rooks:
        total += 50

    return total

def __get_board_total_score(board: chess.Board, color: chess.Color) -> int:

    color_score = get_board_score(board, color)
    opposite_color_score = get_board_score(board, not color)
    return color_score - opposite_color_score