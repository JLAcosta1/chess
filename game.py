def chess():
  
  class Board:

    def __init__(self) -> None:
      self.spotList = []

      for i in range(8):
        self.spotList.append(list())

        for j in range(8):
          self.spotList[i].append(Spot(chr(104-i), j+1))

          if i == 0 or i == 7:
            color = 'Black' if i == 0 else 'White'
            if j == 0:
              # Sets Rooks

              current = self.spotList[i][j]
              current.setPiece(Rook(color))

            elif j == 1:
              # Sets Knight
              current = self.spotList[i][j]
              current.setPiece(Knight(color))
              

            elif j == 2:
              # Sets Bishop
              current = self.spotList[i][j]
              current.setPiece(Bishop(color))


            elif j == 3:
              # Sets Queen
              current = self.spotList[i][j]
              current.setPiece(Queen(color))


            elif j == 4:
              # Sets King
              current = self.spotList[i][j]
              current.setPiece(King(color))

            elif j == 5:
              # Sets Bishop
              current = self.spotList[i][j]
              current.setPiece(Bishop(color))

            elif j == 6:
              # Sets Knights
              current = self.spotList[i][j]
              current.setPiece(Knight(color))

            elif j == 7:
              # Sets Rook
              current = self.spotList[i][j]
              current.setPiece(Rook(color))

          elif i == 1:
            # Sets Pawns for File 2
            current = self.spotList[i][j]
            current.setPiece(Pawn('Black'))

          elif i == 6:
            # Sets Pawns for File 3
            current = self.spotList[i][j]
            current.setPiece(Pawn('White'))

    def movePiece(self, string):

      if len(string) == 2:
        # This is a pawn move
        file = int(ord(string[0]) - 97 )
        rank = int(string[1])

        pawnsInFile = []

        for i in range(len(self.spotList)):
          current = self.spotList[i][file]

          print(type(current))
          print(type(current.getPiece()))
          print(current.getPiece())
          test = isinstance(current.getPiece(), Pawn)
          print(test)
          print(current.getColor())
          if test and current.getColor() == 'W':
            print('hellow from if test')

            pawnsInFile.append(current)

        print(pawnsInFile)

        if len(pawnsInFile) == 1:
          old = pawnsInFile[0]
          new = self.spotList[rank][file]
          new.setPiece(old.getPiece())
          old.setPiece(None)
    


      elif len(string) == 3:
        # This is a non-pawn move
        pass

      elif len(string) == 4:
        # This is a non-pawn move on a piece that has more than one appearance on the board. A way to specifiy which piece
        pass


    def getBoardById(self): 
      '''Returns an 8x8 grid showing tite (Spot) ID'''
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getId(), end=' ')

        print()

    def getBoardBySymbol(self):
      '''Returns an 8x8 grid showing Pieces on Board by their Symbol'''
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getSymbol(), end=' ')

        print()

    def getBoardByColor(self):
      '''Returns an 8x8 grid showing Pieces on Board by their Color'''
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getColor(), end=' ')

        print()


  # An object for each Spot on Board

  class Spot:

    def __init__(self, rank, file) -> None:
      self.id = str(rank) + str(file)
      self.piece = None

    def setPiece(self, piece):
      '''Assign Piece Object to Spot'''
      self.piece = piece

    def getId(self):
      '''Return id value of Spot'''
      return self.id

    def getSymbol(self):
      '''Return Symbol attribute of Piece assigned to Spot'''
      if self.piece == None:
        return '-'
      return self.piece.getSymbol()

    def getColor(self):
      '''Return Color attribute of Piece assigned to Spot'''
      if self.piece == None:
        return '-'
      return self.piece.getColor()

    def getPiece(self):
      '''Return Piece attrivute of Piece assigned to Spot'''
      return self.piece


  # Base Class for All Pieces for Chess

  class Piece:
    def __init__(self, symbol, color) -> None:
      self.symbol = symbol
      self.color = color

    def getSymbol(self):
      '''Return Symbol value of Piece'''
      return self.symbol

    def getColor(self):
      '''Return first character of Color value of Piece'''
      return self.color[0]



  class Pawn(Piece):
    def __init__(self, color) -> None:
      super().__init__("P", color)

  class Rook(Piece):
    def __init__(self, color) -> None:
      super().__init__('R', color)

  class Knight(Piece):
    def __init__(self, color) -> None:
      super().__init__('N', color)

  class Bishop(Piece):
    def __init__(self, color) -> None:
      super().__init__('B', color)

  class Queen(Bishop, Rook):
    def __init__(self, color) -> None:
      Piece.__init__(self, 'Q', color)

  class King(Piece):
    def __init__(self, color) -> None:
      super().__init__('K', color)



  class Player:
    pass

  game = Board()


  game.getBoardById()
  game.getBoardByColor()
  game.getBoardBySymbol()

  game.movePiece('e4')

  game.getBoardById()
  game.getBoardByColor()

  return game.getBoardBySymbol()

