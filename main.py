import random

choiceCount = 0
inv = {"KEY": 0}

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

    def generateRooms(xDim, yDim, xOff, yOff):
        for x in range(xDim):
            for y in range(yDim):
                Room(x + xOff, y + yOff, "EMPTY")

    def checkForWall(x1, y1, x2, y2):
        if (x1, y1, x2, y2) in Room.walls or (x2, y2, x1, y1) in Room.walls:
            return True
        else:
            return False

    def setRoomType(xPos, yPos, type):
        for room in Room.rooms:
            if room.xPos == xPos and room.yPos == yPos:
                room.type = type

    def getRoomType(xPos, yPos):
        for room in Room.rooms:
            if room.xPos == xPos and room.yPos == yPos:
                return room.type

    def getRoom(xPos, yPos):
        for room in Room.rooms:
            if room.xPos == xPos and room.yPos == yPos:
                return room



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
            for wall in Wall.walls:
                if wall.pos == pos or wall.pos == (pos[2], pos[3], pos[0], pos[1]):
                    return wall.type
            return False
        else:
            return False

    def getWall(pos):
        for wall in Wall.walls:
            if wall.pos == pos:
                return wall

        print("No wall stupid")
        


class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    

    def move(self, xDel, yDel):
        def step(xDel, yDel): # im so sorry
            self.xPos += xDel
            self.yPos += yDel
            if Room.getRoomType(self.xPos, self.yPos) == "KEYPICKUP":
                print("There is a key on the ground of this room")
                while True:
                    opt = input("Do you pick up the key? - ")
                    if opt == "yes" or opt == "y":
                        inv["KEY"] += 1
                        Room.getRoom(self.xPos, self.yPos).type = "EMPTY"
                        print(f"You picked up the key ({inv["KEY"]} keys available)")
                        break

                    elif opt == "no" or opt == "n":
                        print("You leave the key on the ground")
                        break

                    else:
                        print("Invalid input (try yes or no)")

        xTar = self.xPos + xDel
        yTar = self.yPos + yDel
        if Room.exists(self.xPos + xDel, self.yPos + yDel):
            qerWallPos = (self.xPos, self.yPos, xTar, yTar)
            qerWall = Wall.checkForWall(qerWallPos)

            if not qerWall:
                step(xDel, yDel)
                print(f"Moved the player to the room at {self.xPos}, {self.yPos}")

            elif qerWall == "OPENDOOR":
                step(xDel, yDel)
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
                            print(f"Player unlocked and moved through a door to {self.xPos}, {self.yPos}")
                            break
                        elif opt == "no" or opt == "n":
                            print("The door stays locked")
                            break
                        else:
                            print("Invalid input (try yes or no)")

                elif inv["KEY"] < 1:
                    print("You do not have a key to open this door")


            else:

                print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.xPos}, {self.yPos}")
        else:
            print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.xPos}, {self.yPos}")
    
player = Player(1, 1)

Room.generateRooms(3, 3, 0, 0)
Room.setRoomType(2, 1, "KEYPICKUP")

Wall((1, 1, 2, 1), "SOLID")
Wall((1, 1, 0, 1), "OPENDOOR")
Wall((0, 1, 0 ,2), "SOLID")
Wall((1, 0, 0, 0), "SOLID")
Wall((0, 1, 0, 0), "LOCKEDDOOR")

Room.generateRooms(3, 3, 0, -3)
Wall((1, 0, 1, -1), "SOLID")
Wall((2, 0, 2, -1), "SOLID")


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
    print()
