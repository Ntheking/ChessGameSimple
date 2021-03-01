import copy
from random import random
import uuid


class Piece():
	pieceCol = "w"
	uniqIdent = 0
	def __init__(self, setCol):
		self.pieceCol = setCol
		self.uniqIdent = uuid.uuid4()
	def __eq__(self, other):
		if not isinstance(other, Piece):
			return False
		elif other==None:
			return False
		elif self.uniqIdent == other.uniqIdent:
			return True
		return False
	def findPosition(self, boardObj):
		#if boardObj == None:
			#boardObj = boardItem
		for rowPos, row in enumerate(boardObj.board):
			for colPos, square in enumerate(row):
				if square == self:
					return (rowPos, colPos)
		print("ERROR")
	def __repr__(self):
		return str(self)
	def controlledMove(self, location, boardObj, col):
		if self.pieceCol != col:
			return False
		for move in self.getMoveData(boardObj):
			if location==move:
				self.move(location, boardObj)
				return
		return False
	def move(self, location, boardObj):
		curCoord = self.findPosition(boardObj)
		boardObj.board[location[0]][location[1]] = boardObj.board[curCoord[0]][curCoord[1]]
		boardObj.board[curCoord[0]][curCoord[1]] = None
		return boardObj.board[location[0]][location[1]]

	def getMoveData(self, board):
		boardInst = board
		return []

class Rook(Piece):
	val = 5
	identity = "Rook"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		if coords == None:
			print("HELLO")
		coords = self.findPosition(board)
		i = coords[0]+1
		while i < 8:
			if boardInst.board[i][coords[1]] != None:
				if boardInst.board[i][coords[1]].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, coords[1]))
					break
			possibleMoves.append((i, coords[1]))
			i+=1
		i = coords[0]-1
		while i >= 0:
			if boardInst.board[i][coords[1]] != None:
				if boardInst.board[i][coords[1]].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, coords[1]))
					break
			possibleMoves.append((i, coords[1]))
			i-=1
		i = coords[1]+1
		while i < 8:
			if boardInst.board[coords[0]][i] != None:
				if boardInst.board[coords[0]][i].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((coords[0], i))
					break
			possibleMoves.append((coords[0], i))
			i+=1
		i = coords[1]-1
		while i >= 0:
			if boardInst.board[coords[0]][i] != None:
				if boardInst.board[coords[0]][i].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((coords[0], i))
					break
			possibleMoves.append((coords[0], i))
			i-=1
		return possibleMoves
	def __str__(self):
		if self.pieceCol == 'b':
			return '♖'
		else:
			return "♜"

class Bishop(Piece):
	val = 3.2
	identity = "Bishop"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		i = coords[0] + 1
		k =coords[1] + 1
		while i < 8 and k < 8:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i+=1
			k+=1
		i = coords[0] - 1
		k =coords[1] + 1
		while i >= 0 and k < 8:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i-=1
			k+=1
		i = coords[0] - 1
		k =coords[1] - 1
		while i >= 0 and k >= 0:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i-=1
			k-=1
		i = coords[0] + 1
		k = coords[1] - 1
		while i < 8 and k >= 0:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i+=1
			k-=1
		return possibleMoves;
	
	def __str__(self):
		if self.pieceCol == 'b':
			return '♗'
		else:
			return "♝"

class Queen(Piece):
	val = 9
	identity = "Queen"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		i = coords[0] + 1
		k =coords[1] + 1
		while i < 8 and k < 8:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i+=1
			k+=1
		i = coords[0] - 1
		k =coords[1] + 1
		while i >= 0 and k < 8:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i-=1
			k+=1
		i = coords[0] - 1
		k =coords[1] - 1
		while i >= 0 and k >= 0:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i-=1
			k-=1
		i = coords[0] + 1
		k = coords[1] - 1
		while i < 8 and k >= 0:
			if boardInst.board[i][k] != None:
				if boardInst.board[i][k].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, k))
					break
			possibleMoves.append((i, k))
			i+=1
			k-=1
		i = coords[0]+1
		while i < 8:
			if boardInst.board[i][coords[1]] != None:
				if boardInst.board[i][coords[1]].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, coords[1]))
					break
			possibleMoves.append((i, coords[1]))
			i+=1
		i = coords[0]-1
		while i >= 0:
			if boardInst.board[i][coords[1]] != None:
				if boardInst.board[i][coords[1]].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((i, coords[1]))
					break
			possibleMoves.append((i, coords[1]))
			i-=1
		i = coords[1]+1
		while i < 8:
			if boardInst.board[coords[0]][i] != None:
				if boardInst.board[coords[0]][i].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((coords[0], i))
					break
			possibleMoves.append((coords[0], i))
			i+=1
		i = coords[1]-1
		while i >= 0:
			if boardInst.board[coords[0]][i] != None:
				if boardInst.board[coords[0]][i].pieceCol == self.pieceCol:
					break
				else:
					possibleMoves.append((coords[0], i))
					break
			possibleMoves.append((coords[0], i))
			i-=1
		return possibleMoves;
	def __str__(self):
		if self.pieceCol == 'b':
			return '♕'
		else:
			return "♛"

class Pawn(Piece):
	val = 1
	identity = "Pawn"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		if self.pieceCol == 'w':
			if coords[0]-1 < 0:
				return []
			if boardInst.board[coords[0]-1][coords[1]] == None:
				possibleMoves.append((coords[0]-1, coords[1]))
				if coords[0] == 6 and boardInst.board[coords[0]-2][coords[1]] == None:
					possibleMoves.append((coords[0]-2, coords[1]))
			if coords[1] + 1 < 8:
				if boardInst.board[coords[0]-1][coords[1]+1] != None:
					if boardInst.board[coords[0]-1][coords[1]+1].pieceCol != self.pieceCol:
						possibleMoves.append((coords[0]-1, coords[1]+1))
			if coords[1] - 1 >= 0:
				if boardInst.board[coords[0]-1][coords[1]-1] != None:
					if boardInst.board[coords[0]-1][coords[1]-1].pieceCol != self.pieceCol:
						possibleMoves.append((coords[0]-1, coords[1]-1))
		elif self.pieceCol == 'b':
			if coords[0]+1 > 7:
				return []
			if boardInst.board[coords[0]+1][coords[1]] == None:
				possibleMoves.append((coords[0]+1, coords[1]))
				if coords[0] == 1 and boardInst.board[coords[0]+2][coords[1]] == None:
					possibleMoves.append((coords[0]+2, coords[1]))
			if coords[1] + 1 < 8:
				if boardInst.board[coords[0]+1][coords[1]+1] != None:
					if boardInst.board[coords[0]+1][coords[1]+1].pieceCol != self.pieceCol:
						possibleMoves.append((coords[0]+1, coords[1]+1))
			if coords[1] - 1 >= 0:
				if boardInst.board[coords[0]+1][coords[1]-1] != None:
					if boardInst.board[coords[0]+1][coords[1]-1].pieceCol != self.pieceCol:
						possibleMoves.append((coords[0]+1, coords[1]-1))

				

		return possibleMoves;
	def __str__(self):
		if self.pieceCol == 'b':
			return '♙'
		else:
			return "♟︎"

class King(Piece):
	val = 10000
	identity = "King"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		checkMov = []
		checkMov.append((coords[0]+1, coords[1]))
		checkMov.append((coords[0]-1, coords[1]))
		checkMov.append((coords[0], coords[1]+1))
		checkMov.append((coords[0], coords[1]-1))
		checkMov.append((coords[0]+1, coords[1]+1))
		checkMov.append((coords[0]+1, coords[1]-1))
		checkMov.append((coords[0]-1, coords[1]+1))
		checkMov.append((coords[0]-1, coords[1]-1))
		for move in checkMov:
			if move[0]<8 and move[0] >= 0 and move[1] < 8 and move[1] >= 0:
				if boardInst.board[move[0]][move[1]] == None or boardInst.board[move[0]][move[1]].pieceCol != self.pieceCol:
					if not boardInst.isCheck(move, coords):
						possibleMoves.append(move)
		return possibleMoves
	def __str__(self):
		if self.pieceCol == 'b':
			return '♔'
		else:
			return "♚"

class Horse(Piece):
	val = 3
	identity = "Horse"
	def getMoveData(self, board):
		boardInst = board
		possibleMoves = []
		coords = self.findPosition(board)
		checkMov = []
		checkMov.append((coords[0]+2, coords[1]+1))
		checkMov.append((coords[0]+2, coords[1]-1))
		checkMov.append((coords[0]-2, coords[1]+1))
		checkMov.append((coords[0]-2, coords[1]-1))
		checkMov.append((coords[0]+1, coords[1]+2))
		checkMov.append((coords[0]+1, coords[1]-2))
		checkMov.append((coords[0]-1, coords[1]+2))
		checkMov.append((coords[0]-1, coords[1]-2))
		for move in checkMov:
			if move[0]<8 and move[0] >= 0 and move[1] < 8 and move[1] >= 0:
				if boardInst.board[move[0]][move[1]] == None or boardInst.board[move[0]][move[1]].pieceCol != self.pieceCol:
					possibleMoves.append(move)
		return possibleMoves;
	def __str__(self):
		if self.pieceCol == 'b':
			return '♘'
		else:
			return "♞"

class Board():
	board = []
	blackFormat = '\033[7m'
	blackFormatEnd = '\033[0m'
	#instatiating and setting up board array
	def __init__ (self):
		row1=[Rook('b'), Horse('b'), Bishop('b'), King('b'), Queen('b'), Bishop('b'), Horse('b'), Rook('b')]
		row2=[Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'), Pawn('b'),Pawn('b'), Pawn('b')]
		row4=[Rook('w'), Horse('w'), Bishop('w'), King('w'), Queen('w'), Bishop('w'), Horse('w'), Rook('w')]
		row3=[Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w'), Pawn('w')]

		midRow = [None, None, None, None, None, None, None, None]
		self.board = [row1, row2, copy.deepcopy(midRow), copy.deepcopy(midRow), copy.deepcopy(midRow), copy.deepcopy(midRow), row3, row4]
	#displaying board in nice format
	def display(self):
		for row in self.board:
			for square in row:
				#ensuring that empty spaces aren't shown.
				if square == None:
					print('  ', end='')
					continue
				print(square, end=' ')
			print('')
	
	def isCheckMate(self,kingPos):
		kingObj = self.board[kingPos[0]][kingPos[1]]
		if not self.isCurCheck(kingObj, kingPos):
			return False
		if len(kingObj.getMoveData(self)) > 0:
			return False
		boardCopy = copy.deepcopy(self)
		#copiedKingObj = boardCopy.board[kingPos[0]][kingPos[1]]
		for row in boardCopy.board:
			for piece in row:
				if piece == None:
					continue
				if piece.identity == "King":
					continue
				if piece.pieceCol != kingObj.pieceCol:
					continue
				for move in piece.getMoveData(self):
					piece.move(move)
					if self.isCurCheck(kingObj):
						continue
					return False
		return True




	def isCurCheck(self,kingObj, kingCoords):
		for row in self.board:
			for piece in row:
				if piece == None or piece.identity == "King":
					continue
				for move in piece.getMoveData(self):
					if move == kingCoords and piece.pieceCol != kingObj.pieceCol:
						return True
		return False

	def isStaleMate(self):
		wKingPos = self.getKingPos('w')
		bKingPos = self.getKingPos('b')
		wKingObj = self.board[wKingPos[0]][wKingPos[1]]
		bKingObj = self.board[bKingPos[0]][bKingPos[1]]
		totalBlackMoves = 0
		totalWhiteMoves = 0
		if self.isCurCheck(wKingObj, wKingPos) or self.isCurCheck(bKingObj, bKingPos):
			return False
		for row in self.board:
			for piece in row:
				if piece == None:
					continue
				if piece.pieceCol == 'b':
					totalBlackMoves += len(piece.getMoveData(self))	
				else:
					totalWhiteMoves += len(piece.getMoveData(self))
		if totalBlackMoves == 0 or totalWhiteMoves == 0:
			return True
		return False
	def getKingPos(self, col):
		for row in self.board:
			for piece in row:
				if piece == None:
					continue
				if piece.identity == "King" and piece.pieceCol == col:
					return piece.findPosition(self)
		return -1


	def isCheck(self, posGo, kingPos):
		boardCopy = copy.deepcopy(self)
		kingObj = boardCopy.board[kingPos[0]][kingPos[1]].move(posGo, boardCopy)
		if kingObj == False:
			return -1
		for row in boardCopy.board:
			for piece in row:
				if piece == None:
					continue
				if piece.identity == "King":
					continue
				for move in piece.getMoveData(boardCopy):
					if move == posGo and piece.pieceCol != kingObj.pieceCol:
						#print(boardReset)
						return True
		return False


# boardItem  = Board()
# boardItem.display()
# boardItem.board[6][1].controlledMove((5,1), boardItem, 'w')
# boardItem.display()












boardItem = Board()
curTurn = 'w'
while True:
	boardItem.display()
	if curTurn == 'w':
		print("Which Piece Would White Like to Move?")
		row = int(input("Row?"))
		col = int(input("Column?"))
		print("Where Would White Like to Move?")
		rowGo = int(input("Row?"))
		colGo = int(input("Column?"))
		if not boardItem.board[row][col].move((rowGo, colGo), boardItem):
			print("That is not a valid move")
			continue
		else: curTurn = 'b'
	elif curTurn == 'b':
		print("Which Piece Would Black Like to Move?")
		row = int(input("Row?"))
		col = int(input("Column?"))
		print("Where Would White Black to Move?")
		rowGo = int(input("Row?"))
		colGo = int(input("Column?"))
		if not boardItem.board[row][col].controlledMove((rowGo, colGo), boardItem, curTurn):
			print("That is not a valid move")
			continue
		else: curTurn = 'w'
	if boardItem.isCheckMate(boardItem.getKingPos('b')):
		print("White Wins!")
		break
	elif boardItem.isCheckMate(boardItem.getKingPos('w')):
		print("Black Wins!")
		break
	elif boardItem.isStaleMate():
		print("Stale Mate")
		break
	kp = boardItem.getKingPos(curTurn)
	if boardItem.isCurCheck(boardItem.board[kp[0]][kp[1]], kp):
		print("Check")
		
	











