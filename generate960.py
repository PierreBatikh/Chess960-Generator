import sys
import chess
import chess.svg

while True:
    try:
        position = int(input("Enter a valid (0 -> 959) chess960 position: "))
        if not 0 <= position < 960:
            continue
        else:
            break
    except ValueError:
        print("Rerun the script please!")
        sys.exit()

chess_pos = chess.Board.from_chess960_pos(position)
board = chess.Board(chess_pos.fen())
svgg = chess.svg.board(board)
with open(f"svg_pos{position}.svg", "w", encoding="utf-8") as f:
    f.write(svgg)
print("The photo is saved to the directory this script was run from, open the photo in your browser!")
