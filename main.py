import random

choiceCount = 0
inv = {"KEY": 0}

class RoomType:
    roomtypes = []

    def __init__(self, type, rarity):
        self.type = type
        self.rarity = rarity
        RoomType.roomtypes.append(self)



class Room:
    rooms = []

    def __init__(self, xPos, yPos, type):
        self.xPos = xPos
        self.yPos = yPos
        self.type = type
        Room.rooms.append(self)

    def exists(xQer, yQer):
        for room in Room.rooms:
            if room.xPos == xQer and room.yPos == yQer:
                return True
            
        return False

    def refreshRooms():
        for x in range(3):
            for y in range(3):
                Room(x, y, "nill")

    def checkForWall(x1, y1, x2, y2):
        if (x1, y1, x2, y2) in Room.walls or (x2, y2, x1, y1) in Room.walls:
            return True
        else:
            return False



class Wall:
    walls = set()
    wallPoss = set()

    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        Wall.walls.add(self)
        Wall.wallPoss.add(pos)
        
    def checkForWall(pos):
        if pos in Wall.wallPoss or (pos[2], pos[3], pos[0], pos[1]) in Wall.wallPoss:
            type = "nill"
            for wall in Wall.walls:
                if wall.pos == pos or wall.pos == (pos[2], pos[3], pos[0], pos[1]):
                    type = wall.type

            return type
        else:
            return False

    def getWall(pos):
        for wall in Wall.walls:
            if wall.pos == pos:
                return wall

        print("No wall stupid")


    
Room.refreshRooms()
Wall((1, 1, 2, 1), "SOLID")
Wall((1, 1, 0, 1), "OPENDOOR")
Wall((0, 1, 0 ,2), "SOLID")
Wall((1, 0, 0, 0), "SOLID")
Wall((0, 1, 0, 0), "LOCKEDDOOR")

class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def move(self, xDel, yDel):
        xTar = self.xPos + xDel
        yTar = self.yPos + yDel
        if Room.exists(self.xPos + xDel, self.yPos + yDel):
            qerWallPos = (self.xPos, self.yPos, xTar, yTar)
            qerWall = Wall.checkForWall(qerWallPos)

            if not qerWall:
                self.xPos += xDel
                self.yPos += yDel
                print(f"Moved the player to the room at {self.xPos}, {self.yPos}")

            elif qerWall == "OPENDOOR":
                self.xPos += xDel
                self.yPos += yDel
                print(f"Player moved through an open door to the room at {self.xPos}, {self.yPos}")

            elif qerWall == "LOCKEDDOOR":
                print("There is a locked door in the way of the player moving that way, try to unlock it or try a different direction")
                if inv["KEY"] > 0:
                    while True:
                        opt = input(f"Do you unlock it? ({inv["KEY"]} keys available) - ")
                        if opt == "yes" or opt == "y":
                            wall = Wall.getWall(qerWallPos)
                            wall.type = "OPENDOOR"
                            inv["KEY"] -= 1
                            self.xPos += xDel
                            self.yPos += yDel
                            print(f"Player unlocked and moved through a door at {self.xPos}, {self.yPos}")
                            break
                        elif opt == "no" or opt == "n":
                            print("The door stays locked")
                            break
                        else:
                            print("Invalid Operation")

                elif inv["KEY"] < 1:
                    print("You do not have a key to open this door")


            else:

                print("There is a wall in the way of the player moving that way, try a different direction")
        else:
            print("There is a wall in the way of the player moving that way, try a different direction")
    
player = Player(1, 1)




while True:
    choiceCount += 1
    print(f">-----------------< Move {choiceCount} >-----------------<")
    dir = input("Where do you go? - ")

    if dir == "forward" or dir == "for" or dir == "f" or dir == "w":
        player.move(1, 0)
    elif dir == "right" or dir == "rit" or dir == "r" or dir == "d":
        player.move(0, 1)
    elif dir == "backward" or dir == "bac" or dir == "b" or dir == "s":
        player.move(-1, 0)
    elif dir == "left" or dir == "lef" or dir == "l" or dir == "a":
        player.move(0, -1)
    else:
        print("Invalid direction (try forward, right, left, or backward, or try inputing their first letter)")
