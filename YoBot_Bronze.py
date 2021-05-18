# This file is part of YoBot_Bronze UCI Chess Engine.
# Copyright (C) 2021- Yohaan Seth Nathan (TheYoBots)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# You should have received a copy of the MIT License along with this 
# UCI Chess Engine. If not, view this https://opensource.org/licenses/MIT

import chess
import random
import sys

LOGFILE = "logs.txt"

def main():

    board = chess.Board()

    while True:
        msg = input()

        f = open(LOGFILE, "a")
        f.write(f"> {msg}\n")
        f.close()

        command(board, msg)

def sendResponse(msg: str):
    f = open(LOGFILE, "a")
    f.write(f"< {msg}\n")
    f.close()
    print(msg)

def command(board: chess.Board, msg: str):
    if msg == "quit":
        sys.exit(0)

    if msg == "uci":
        sendResponse("id name YoBot Bronze")
        sendResponse("id author Yohaan Seth Nathan")
        sendResponse("option name Debug Log File type string default")
        sendResponse("option name Contempt type spin default 24 min -100 max 100")
        sendResponse("option name Analysis Contempt type combo default Both var Off var White var Black var Both")
        sendResponse("option name Threads type spin default 1 min 1 max 512")
        sendResponse("option name Hash type spin default 16 min 1 max 131072")
        sendResponse("option name Clear Hash type button")
        sendResponse("option name Ponder type check default false")
        sendResponse("option name MultiPV type spin default 1 min 1 max 500")
        sendResponse("option name Skill Level type spin default 20 min 0 max 20")
        sendResponse("option name Move Overhead type spin default 30 min 0 max 5000")
        sendResponse("option name Minimum Thinking Time type spin default 20 min 0 max 5000")
        sendResponse("option name Slow Mover type spin default 84 min 10 max 1000")
        sendResponse("option name nodestime type spin default 0 min 0 max 10000")
        sendResponse("option name UCI_Chess960 type check default false")
        sendResponse("option name UCI_AnalyseMode type check default false")
        sendResponse("option name SyzygyPath type string default <empty>")
        sendResponse("option name SyzygyProbeDepth type spin default 1 min 1 max 100")
        sendResponse("option name Syzygy50MoveRule type check default true")
        sendResponse("option name SyzygyProbeLimit type spin default 7 min 0 max 7")
        sendResponse("uciok")
        return

    if msg == "isready":
        sendResponse("readyok")
        return

    if msg == "ucinewgame":
        return

    if "position startpos moves" in msg:
        moves = msg.split(" ")[3:]
        board.clear()
        board.set_fen(chess.STARTING_FEN)
        for move in moves:
            board.push(chess.Move.from_uci(move))
        return

    if "position fen" in msg:
        fen = " ".join(msg.split(" ")[2:])
        board.set_fen(fen)
        return

    if msg[0:2] == "go":
        _move = random.choice(list(board.legal_moves)) 
        sendResponse(f"bestmove {_move}")
        return

main()