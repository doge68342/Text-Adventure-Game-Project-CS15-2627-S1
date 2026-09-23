import random

choiceCount = 0
inv = {"KEYBASIC": 0,
       "KEYORNATE": 0}

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

    def invQer(self):
        if inv["KEYBASIC"] > 0:
            print(f"You have {inv['KEYBASIC']} basic key(s)")
        if inv["KEYORNATE"] > 0:
            print(f"You have {inv['KEYORNATE']} ornate key(s)")

    def spacQer(self):
        validDirs = []
        qerWallPos = (self.xPos, self.yPos, self.xPos + 1, self.yPos)
        qerWall = Wall.checkForWall(qerWallPos)
        if Room.exists(self.xPos + 1, self.yPos) and not qerWall or qerWall == "OPENDOOR":
            validDirs.append("forward")

        qerWallPos = (self.xPos, self.yPos, self.xPos - 1, self.yPos)
        qerWall = Wall.checkForWall(qerWallPos)
        if Room.exists(self.xPos -1, self.yPos) and not qerWall or qerWall == "OPENDOOR":
            validDirs.append("backward")

        qerWallPos = (self.xPos, self.yPos, self.xPos, self.yPos + 1)
        qerWall = Wall.checkForWall(qerWallPos)
        if Room.exists(self.xPos, self.yPos + 1) and not qerWall or qerWall == "OPENDOOR":
            validDirs.append("right")

        qerWallPos = (self.xPos, self.yPos, self.xPos, self.yPos - 1)
        qerWall = Wall.checkForWall(qerWallPos)
        if Room.exists(self.xPos, self.yPos - 1) and not qerWall or qerWall == "OPENDOOR":
            validDirs.append("left")

        out = "Player can move "
        if len(validDirs) == 1:
            out += validDirs[0]
        elif len(validDirs) == 2:
            out += validDirs[0]
            out += " or "
            out += validDirs[1]
        elif len(validDirs) == 3:
            out += validDirs[0]
            out += ", "
            out += validDirs[1]
            out += " or "
            out += validDirs[2]
        elif len(validDirs) == 4:
            out += validDirs[0]
            out += ", "
            out += validDirs[1]
            out += ", "
            out += validDirs[2]
            out += " or "
            out += validDirs[3]
        else:
            out += "nowhere (uh oh)"   
        print(out)


    def move(self, xDel, yDel):
        def step(xDel, yDel): # im so sorry
            self.xPos += xDel
            self.yPos += yDel
            if Room.getRoomType(self.xPos, self.yPos) == "KEYBASICPICKUP":
                print("There is a key on the ground of this room")
                while True:
                    opt = input("Do you pick up the key? - ")
                    if opt == "yes" or opt == "y":
                        inv["KEYBASIC"] += 1
                        Room.getRoom(self.xPos, self.yPos).type = "EMPTY"
                        print(f"You picked up the key ({inv["KEYBASIC"]} keys available)")
                        break

                    elif opt == "no" or opt == "n":
                        print("You leave the key on the ground")
                        break

                    else:
                        print("Invalid input (try yes or no)")

            if Room.getRoomType(self.xPos, self.yPos) == "EMPTYPEDESTAL":
                print("There is an empty pedestal in this room")

            if Room.getRoomType(self.xPos, self.yPos) == "KEYORNATEPICKUP":
                print("There is a ornate golden key on a small wooden pedestal in this room")
                while True:
                    opt = input("Do you pick up the ornate key? - ")
                    if opt == "yes" or opt == "y":
                        inv["KEYORNATE"] += 1
                        Room.getRoom(self.xPos, self.yPos).type = "EMPTYPEDESTAL"
                        print(f"You picked up the ornate key ({inv["KEYORNATE"]} keys available)")
                        break

                    elif opt == "no" or opt == "n":
                        print("You leave the ornate key on the pedestal")
                        break

                    else:
                        print("Invalid input (try yes or no)")

    

        xTar = self.xPos + xDel
        yTar = self.yPos + yDel
        if Room.exists(self.xPos + xDel, self.yPos + yDel):
            qerWallPos = (self.xPos, self.yPos, xTar, yTar)
            qerWall = Wall.checkForWall(qerWallPos)

            if not qerWall:
                print(f"Moved the player to the room at {self.xPos + xDel}, {self.yPos + yDel}")
                step(xDel, yDel)

            elif qerWall == "OPENDOOR":
                print(f"Player moved through an open door to the room at {self.xPos + xDel}, {self.yPos + yDel}")
                step(xDel, yDel)


            elif qerWall == "LOCKEDDOORBASIC":
                print("There is a locked door in the way of the player moving that way, try to unlock it or try a different direction")
                if inv["KEYBASIC"] > 0:
                    while True:
                        opt = input(f"Do you unlock it? ({inv["KEYBASIC"]} keys available) - ")
                        if opt == "yes" or opt == "y":
                            wall = Wall.getWall(qerWallPos)
                            wall.type = "OPENDOOR"
                            inv["KEYBASIC"] -= 1
                            print(f"Player unlocked and moved through a door to {self.xPos + xDel}, {self.yPos + yDel}")
                            step(xDel, yDel)
                            break
                        elif opt == "no" or opt == "n":
                            print("The door stays locked")
                            break
                        else:
                            print("Invalid input (try yes or no)")

                elif inv["KEYBASIC"] < 1:
                    print("You do not have a key to open this door")

            elif qerWall == "LOCKEDDOORORNATE":
                print("There is an ornate locked door in the way of the player moving that way, try to unlock it or try a different direction")
                if inv["KEYORNATE"] > 0:
                    while True:
                        opt = input(f"Do you unlock it? ({inv["KEYORNATE"]} keys available) - ")
                        if opt == "yes" or opt == "y":
                            wall = Wall.getWall(qerWallPos)
                            wall.type = "OPENDOOR"
                            inv["KEYORNATE"] -= 1
                            print(f"Player unlocked and moved through a door to {self.xPos + xDel}, {self.yPos + yDel}")
                            step(xDel, yDel)
                            break
                        elif opt == "no" or opt == "n":
                            print("The ornate door stays locked")
                            break
                        else:
                            print("Invalid input (try yes or no)")

                elif inv["KEYORNATE"] < 1:
                    print("You do not have a key to open this door")

            else:

                print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.xPos}, {self.yPos}")
        else:
            print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.xPos}, {self.yPos}")
    
player = Player(1, 1)

Room.generateRooms(3, 3, 0, 0)
Room.setRoomType(2, 1, "KEYBASICPICKUP")
Room.setRoomType(0, 0, "KEYORNATEPICKUP")

Wall((1, 1, 2, 1), "SOLID")
Wall((1, 1, 0, 1), "OPENDOOR")
Wall((0, 1, 0 ,2), "SOLID")
Wall((1, 0, 0, 0), "SOLID")
Wall((0, 1, 0, 0), "LOCKEDDOORBASIC")

Room.generateRooms(1, 1, 1, 3)
Wall((1, 2, 1, 3), "LOCKEDDOORORNATE")
Room.generateRooms(3, 3, 0, 4)



while True:
    choiceCount += 1
    print(f">-----------------< Move {choiceCount} >-----------------<")
    opt = input("Where do you go? - ")

    if opt == "forward" or opt == "for" or opt == "f" or opt == "w":
        player.move(1, 0)
    elif opt == "right" or opt == "rit" or opt == "r" or opt == "d":
        player.move(0, 1)
    elif opt == "backward" or opt == "bac" or opt == "b" or opt == "s":
        player.move(-1, 0)
    elif opt == "left" or opt == "lef" or opt == "l" or opt == "a":
        player.move(0, -1)
    elif opt == "querry" or opt == "qer" or opt == "q":
        player.invQer()
        player.spacQer()
    else:
        print("Invalid input (try forward, right, left, backward, or query, or try inputing their first letters)")
    print()
