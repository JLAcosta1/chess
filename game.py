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
              #Sets Rooks

              current = self.spotList[i][j]
              current.setPiece(Rook(color))

            elif j == 1:

              current = self.spotList[i][j]
              current.setPiece(Knight(color))
              

            elif j == 2:

              current = self.spotList[i][j]
              current.setPiece(Bishop(color))


            elif j == 3:
              current = self.spotList[i][j]
              current.setPiece(Queen(color))


            elif j == 4:
              current = self.spotList[i][j]
              current.setPiece(King(color))

            elif j == 5:
              #Sets Rooks

              current = self.spotList[i][j]
              current.setPiece(Bishop(color))

            elif j == 6:
              #Sets Rooks

              current = self.spotList[i][j]
              current.setPiece(Knight(color))

            elif j == 7:
              #Sets Rooks

              current = self.spotList[i][j]
              current.setPiece(Rook(color))

          elif i == 1:
            current = self.spotList[i][j]
            current.setPiece(Pawn('Black'))

          elif i == 6:
            current = self.spotList[i][j]
            current.setPiece(Pawn('White'))

    
    def getBoardById(self):
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getId(), end=' ')

        print()

    def getBoardBySymbol(self):
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getSymbol(), end=' ')

        print()

    def getBoardByColor(self):
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getColor(), end=' ')

        print()


  class Spot:

    def __init__(self, rank, file) -> None:
      self.id = str(rank) + str(file)
      self.piece = None

    def setPiece(self, piece):
      self.piece = piece

    def getId(self):
      return self.id

    def getSymbol(self):
      if self.piece == None:
        return '-'
      return self.piece.getSymbol()

    def getColor(self):
      if self.piece == None:
        return '-'
      return self.piece.getColor()


  class Piece:
    def __init__(self, symbol, color) -> None:
      self.symbol = symbol
      self.color = color

    def getSymbol(self):
      return self.symbol

    def getColor(self):
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

  class Queen(Piece):
    def __init__(self, color) -> None:
      super().__init__('Q', color)

  class King(Piece):
    def __init__(self, color) -> None:
      super().__init__('K', color)



  class Player:
    pass

  game = Board()


  game.getBoardById()
  game.getBoardByColor()

  return game.getBoardBySymbol()

