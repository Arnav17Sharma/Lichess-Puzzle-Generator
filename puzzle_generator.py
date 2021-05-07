from PIL import Image
from random import randint
import pandas as pd
import chess

# Getting a random puzzle

df = pd.read_csv('./puzzles.csv', nrows=randint(1, 999), dtype=str)
j = df.to_string().split("\n")[-1]
puzzle = j.split()


# Solution moves

moves = []
for k in puzzle[8:]:
	if not k.isdigit():
		moves.append(k)
	else:
		moves.append(k)
		break

# Creating Question board and solution boards

im = Image.open('board.jpg')
new_im = im.copy()
FEN = puzzle[2]
l = FEN.split("/")
l[-1] = l[-1].split()[0]
for j in range(len(l)):
	a = -1 
	for i in l[j]:
		if i.isdigit():
			a+=int(i)
		else:
			a += 1
			if i.isupper():
				piece = Image.open(f'./pieces/WHITE/{i}.png')
			else:
				piece = Image.open(f'./pieces/BLACK/{i}.png')
			new_im.paste(piece, (20 + 66 * (a), 25 + 66 * (j)), piece)
new_im.save('./boards/new_board0.jpg', quality=95)
FEN = " ".join(puzzle[2:8])
FEN1 = FEN
def board(FEN, moves):
	board = chess.Board(FEN)
	im = Image.open('board.jpg')
	for move in range(len(moves)):
		make_move = chess.Move.from_uci(moves[move])
		board.push(make_move)
		print(board)
		new_im = im.copy()
		FEN = board.fen()
		l = FEN.split("/")
		l[-1] = l[-1].split()[0]
		for j in range(len(l)):
			a = -1 
			for i in l[j]:
				if i.isdigit():
					a+=int(i)
				else:
					a += 1
					if i.isupper():
						piece = Image.open(f'./pieces/WHITE/{i}.png')
					else:
						piece = Image.open(f'./pieces/BLACK/{i}.png')
					new_im.paste(piece, (20 + 66 * (a), 25 + 66 * (j)), piece)
		new_im.save(f'./boards/new_board{move+1}.jpg', quality=95)
board(FEN, moves[:-1])

l = []
for i in range(len(moves[:-1])):
	img = Image.open(f'./boards/new_board{i+1}.jpg')
	l.append(img)

gif = Image.new("RGBA", im.size)
gif.save(f'./boards/solution.gif', save_all=True, append_images=l, optimize=True ,duration=1000, loop=0)

print("Puzzle Link -", puzzle[-1])
print("Puzzle Rating -", moves[-1])
