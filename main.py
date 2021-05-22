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

def getBestMove(board: chess.Board) -> chess.Move:

    myColor = board.turn
    globalMaxScore = -sys.maxsize
    bestMoves = []

    for myCandidateMove in list(board.legal_moves):

        board.push(myCandidateMove)

        if board.is_checkmate():
            return myCandidateMove

        candidateMinScore = sys.maxsize

        for opponentCandidateMove in list(board.legal_moves):

            board.push(opponentCandidateMove)
            currentScore = getBoardTotalScore(board, myColor)

            if currentScore < candidateMinScore:
                candidateMinScore = currentScore

            board.pop()

        if candidateMinScore > globalMaxScore:
            globalMaxScore = candidateMinScore
            bestMoves = [myCandidateMove]
        elif candidateMinScore == globalMaxScore:
            bestMoves.append(myCandidateMove)

        board.pop()

    return random.choice(bestMoves)

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

def getBoardTotalScore(board: chess.Board, color: chess.Color) -> int:

    colorScore = getBoardScore(board, color)
    oppositeColorScore = getBoardScore(board, not color)
    return colorScore - oppositeColorScore