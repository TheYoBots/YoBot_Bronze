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