

def floodFill(board, start):
    waiting = [start]
    found = {start}
    while len(waiting) > 0:
        w = waiting.pop()

        for x in get_neighbors(w, board):
            if x not in found:
                r, c = x
                if board[r][c] == '-':
                    found.add(x)
                    waiting.append(x)
    return found


def get_neighbors(v, board):
    r, c = v
    N = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return [(a, b) for a, b in N if 0 <= a < len(board) and 0 <= b < len(board[0])]


board = """
---*****---**
**----***--*-
**--**-----**
----*-*--**--
***--***-****
****--**---**
********-*---
"""

board = [list(b) for b in board[1:].split('\n')]

print(get_neighbors((0, 0), board))

stuff = floodFill(board, (0, 0))
for r, c in stuff:
    board[r][c] = chr(9608)

for r in range(len(board)):
    for c in range(len(board[r])):
        print(board[r][c], end='')
    print()
