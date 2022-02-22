def chess():
  
  class Board:

    def __init__(self) -> None:
      self.spotList = []

      for i in range(8):
        self.spotList.append(list())

        for j in range(8):
          self.spotList[i].append(Spot(chr(104-i), j+1))

          if i == 1:
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

  class Player:
    pass

  game = Board()


  game.getBoardBySymbol()
  return game.getBoardBySymbol()

