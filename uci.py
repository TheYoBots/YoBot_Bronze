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
import main
import sys

logger = logging.getLogger(__name__)

board = chess.Board()


def send_response(msg: str):
    logger.info(f"< {msg}")
    print(msg)


def command_received(msg: str):

    logger.info(f"> {msg}")

    if msg == "uci":

        send_response("id name YoBot Bronze")
        send_response("id author Yohaan Seth Nathan")
        send_response("option name Debug Log File type string default")
        send_response("option name Contempt type spin default 24 min -100 max 100")
        send_response("option name Analysis Contempt type combo default Both var Off var White var Black var Both")
        send_response("option name Threads type spin default 1 min 1 max 512")
        send_response("option name Hash type spin default 16 min 1 max 131072")
        send_response("option name Clear Hash type button")
        send_response("option name Ponder type check default false")
        send_response("option name MultiPV type spin default 1 min 1 max 500")
        send_response("option name Skill Level type spin default 20 min 0 max 20")
        send_response("option name Move Overhead type spin default 30 min 0 max 5000")
        send_response("option name Minimum Thinking Time type spin default 20 min 0 max 5000")
        send_response("option name Slow Mover type spin default 84 min 10 max 1000")
        send_response("option name nodestime type spin default 0 min 0 max 10000")
        send_response("option name UCI_Chess960 type check default false")
        send_response("option name UCI_AnalyseMode type check default false")
        send_response("option name SyzygyPath type string default <empty>")
        send_response("option name SyzygyProbeDepth type spin default 1 min 1 max 100")
        send_response("option name Syzygy50MoveRule type check default true")
        send_response("option name SyzygyProbeLimit type spin default 7 min 0 max 7")
        send_response("uciok")
        return

    elif msg == "isready":
        send_response("readyok")
        return

    elif msg == "ucinewgame":
        return

    elif "position startpos moves" in msg:
        moves = msg.split(" ")[3:]
        board.clear()
        board.set_fen(chess.STARTING_FEN)
        for move in moves:
            board.push(chess.Move.from_uci(move))
        return

    elif "position fen" in msg:
        fen = " ".join(msg.split(" ")[2:])
        board.set_fen(fen)
        return

    elif msg[0:2] == "go":
        _move = main.get_best_move(board) 
        send_response(f"bestmove {_move}")
        return

    elif msg == "quit":
        sys.exit(0)