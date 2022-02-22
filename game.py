def chess():
  
  class Board:

    def __init__(self) -> None:
      self.spotList = []

      for i in range(8):
        self.spotList.append(list())

        for j in range(8):
          self.spotList[i].append(Spot(chr(104-i), j+1))

    
    def getBoardById(self):
      for i in range(len(self.spotList)):

        for j in range(len(self.spotList[i])):
          current = self.spotList[i][j]
          print(current.getId(), end=' ')

        print()

      return None



  class Spot:

    def __init__(self, rank, file) -> None:
      self.id = str(rank) + str(file)
      self.piece = None

    def getId(self):
      return self.id


  class Piece:
    pass

  class Player:
    pass

  game = Board()

  return game.getBoardById()

