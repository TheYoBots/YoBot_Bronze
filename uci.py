import logging
import chess
import core
import sys

logger = logging.getLogger(__name__)

board = chess.Board()

def sendResponse(msg: str):
    logger.info(f"< {msg}")
    print(msg)

def commandReceived(msg: str):

    logger.info(f"> {msg}")

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

    elif msg == "isready":
        sendResponse("readyok")
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
        _move = core.getBestMove(board) 
        sendResponse(f"bestmove {_move}")
        return

    elif msg == "quit":
        sys.exit(0)