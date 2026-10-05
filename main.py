"""
A text based adventure game run through the terminal
"""

from PIL import Image

try:
    image = Image.open("Map-v2.png")
except FileNotFoundError:
    print("cd into the directory of main.py or the program wont be able to open the map image")

choice_count = 0
MAX_HEALTH = 20
inventory = {"KEYBASIC": 0,
             "KEYORNATE": 0,
             "SWORD": 0,
             "HEALTH": MAX_HEALTH,
             "FEMURBONE": 0}

print("Defeat the super evil, evil skeleton made of evil bones")
print()

def win_game() -> None:
    """
    Call when win
    """
    while True:
        input(f"horay{chr(33)} You defeated the skeleton and won{chr(33)} You can now close the program")

def lose_game() -> None:
    """
    Call when lose
    """
    while True:
        input("You failed to defeat the skeleton and die, please restart program")

class Room:
    """
    A room that the player can move too and from

    :cvar rooms: table of all rooms made
    """
    rooms = []

    def __init__(self, x_pos, y_pos, room_type):
        """
        Initializes the room

        :param x_pos: x position
        :param y_pos: y position
        :param room_type: the type of room
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.room_type = room_type
        Room.rooms.append(self)
    def exists(x_qer: int, y_qer: int) -> bool:
        """
        Check if room at x, y exists and return true or false if so
        :param x_qer: x
        :param y_qer: y
        :return: return if the room exists
        """
        for room in Room.rooms:
            if room.x_pos == x_qer and room.y_pos == y_qer:
                return True
            
        return False

    def generate_rooms(x_dim: int, y_dim: int, x_off: int, y_off: int) -> None:
        """
        Generates a room at x_dim, y_dim, with offset x_off, y_off

        :param x_dim: the x side length of the room cluster
        :param y_dim: the y side length of the room cluster
        :param x_off: the x offset
        :param y_off: the y offset
        """
        for x in range(x_dim):
            for y in range(y_dim):
                Room(x + x_off, y + y_off, "EMPTY")

    def set_room_type(x_pos: int, y_pos: int, room_type: str) -> None:
        """
        Sets room at x_pos, y_pos to room_type

        :param x_pos: x position of room
        :param y_pos: y position of room
        :param room_type: type of room to change x, y to
        """
        for room in Room.rooms:
            if room.x_pos == x_pos and room.y_pos == y_pos:
                room.room_type = room_type

    def get_room_type(x_pos: int, y_pos: int) -> str:
        """
        Return type of room at x_pos, y_pos

        :param x_pos: x position of room
        :param y_pos: y position of room
        :return: the type of room
        """
        for room in Room.rooms:
            if room.x_pos == x_pos and room.y_pos == y_pos:
                return room.room_type

    def get_room(x_pos: int, y_pos: int) -> "Room":
        """
        Return the room object at x_pos, y_pos

        :param x_pos: x position of room
        :param y_pos: y position of room
        :return: room object (classy)
        """
        for room in Room.rooms:
            if room.x_pos == x_pos and room.y_pos == y_pos:
                return room



class Wall:
    """
    Defines wall that block the player from moving from a certain room to another

    :cvar walls: a set of all of the wall objects
    :cvar wall_positions: all of the wall position tuples
    """
    walls = set()
    wall_positions = set()

    def __init__(self, pos, wall_type):
        """
        Initializes the wall object

        :param pos: tuple of the two tooms that it blocks traversal between
        :param wall_type: the type of wall
        """
        self.pos = pos
        self.wall_type = wall_type
        Wall.walls.add(self)
        Wall.wall_positions.add(pos)
        
    def check_for_wall(pos: tuple) -> bool | str:
        """
        Checks for wall between two room defined by tuple (x1, y1, x2, y2)

        :param pos: defines the two rooms that a wall is checked for between
        :return: return false if no wall, but return the type if there is a wall
        """
        if pos in Wall.wall_positions or (pos[2], pos[3], pos[0], pos[1]) in Wall.wall_positions:
            for wall in Wall.walls:
                if wall.pos == pos or wall.pos == (pos[2], pos[3], pos[0], pos[1]):
                    return wall.wall_type
            return False
        else:
            return False

    def get_wall(pos: tuple) -> "Wall":
        """
        Return wall object from wall defined by tuple (x1, y1, x2, y2)

        :param pos: defines the two rooms that a wall is effective in
        :return: return the wall object
        """
        for wall in Wall.walls:
            if wall.pos == pos:
                return wall

        print("No wall stupid")
        


class Player:
    """
    Player object
    """
    def __init__(self, x_pos: int, y_pos: int):
        """
        Player initialization

        :param x_pos: the x position of where to spawn the player
        :param y_pos: the y position of where to spawn the player
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

    def inventory_query(self) -> None:
        """
        Print everything in players inventory
        """
        if inventory["KEYBASIC"] > 0:
            print(f"You have {inventory['KEYBASIC']} basic key(s)")
        if inventory["KEYORNATE"] > 0:
            print(f"You have {inventory['KEYORNATE']} ornate key(s)")
        if inventory["SWORD"] > 0:
            print(f"You have {inventory['SWORD']} sword(s)")
        if inventory["FEMURBONE"] > 0:
            print(f"You have {inventory['FEMURBONE']} femur bones(s)")
        print(f"You have {inventory["HEALTH"]} / {MAX_HEALTH} health left")
        

    def spatial_query(self) -> None:
        """
        prints directions available for the player to move and locked doors around them
        """
        valid_dirs = []
        query_wall_pos = (self.x_pos, self.y_pos, self.x_pos + 1, self.y_pos)
        query_wall = Wall.check_for_wall(query_wall_pos)
        query_wall = Wall.check_for_wall(query_wall_pos)
        if Room.exists(self.x_pos + 1, self.y_pos):
            if not query_wall or query_wall == "OPENDOOR":
                valid_dirs.append("forward")
            elif query_wall == "LOCKEDDOORBASIC":
                print("There is a locked door in front of you unlockable with a basic key")
            elif query_wall == "LOCKEDDOORORNATE":
                print("There is a locked door in front of you unlockable with an ornate key")

        query_wall_pos = (self.x_pos, self.y_pos, self.x_pos - 1, self.y_pos)
        query_wall = Wall.check_for_wall(query_wall_pos)
        if Room.exists(self.x_pos -1, self.y_pos):
            if not query_wall or query_wall == "OPENDOOR":
                valid_dirs.append("backward")
            elif query_wall == "LOCKEDDOORBASIC":
                print("There is a locked door behind you unlockable with a basic key")
            elif query_wall == "LOCKEDDOORORNATE":
                print("There is a locked door behind you unlockable with an ornate key")

        query_wall_pos = (self.x_pos, self.y_pos, self.x_pos, self.y_pos + 1)
        query_wall = Wall.check_for_wall(query_wall_pos)
        if Room.exists(self.x_pos, self.y_pos + 1):
            if not query_wall or query_wall == "OPENDOOR":
                valid_dirs.append("right")
            elif query_wall == "LOCKEDDOORBASIC":
                print("There is a locked door to your right unlockable with a basic key")
            elif query_wall == "LOCKEDDOORORNATE":
                print("There is a locked door to your right unlockable with an ornate key")

        query_wall_pos = (self.x_pos, self.y_pos, self.x_pos, self.y_pos - 1)
        query_wall = Wall.check_for_wall(query_wall_pos)
        query_wall = Wall.check_for_wall(query_wall_pos)
        if Room.exists(self.x_pos, self.y_pos - 1):
            if not query_wall or query_wall == "OPENDOOR":
                valid_dirs.append("left")
            elif query_wall == "LOCKEDDOORBASIC":
                print("There is a locked door to your left unlockable with a basic key")
            elif query_wall == "LOCKEDDOORORNATE":
                print("There is a locked door to your left unlockable with an ornate key")

        out = "Player can move "
        if len(valid_dirs) == 1:
            out += valid_dirs[0]
        elif len(valid_dirs) == 2:
            out += valid_dirs[0]
            out += " or "
            out += valid_dirs[1]
        elif len(valid_dirs) == 3:
            out += valid_dirs[0]
            out += ", "
            out += valid_dirs[1]
            out += " or "
            out += valid_dirs[2]
        elif len(valid_dirs) == 4:
            out += valid_dirs[0]
            out += ", "
            out += valid_dirs[1]
            out += ", "
            out += valid_dirs[2]
            out += " or "
            out += valid_dirs[3]
        else:
            out += "nowhere (uh oh)"   
        print(out)


    def move(self, x_delta: int, y_delta: int) -> None:
        """
        Attempts to move player x_delta, y_delta

        :param x_delta: the x direction or difference
        :param y_delta: the y direction or difference
        """
        def step(x_delta: int, y_delta: int) -> None:
            """
            Does move player x_delta, y_delta 
            :param x_delta: the x direction or difference
            :param y_delta: the y direction or difference
            """
            self.x_pos += x_delta
            self.y_pos += y_delta
            if Room.get_room_type(self.x_pos, self.y_pos) == "KEYBASICPICKUP":
                print()
                print("There is a key on the ground of this room")
                while True:
                    option = input("Do you pick up the key? - ")
                    if option == "yes" or option == "y":
                        inventory["KEYBASIC"] += 1
                        Room.get_room(self.x_pos, self.y_pos).room_type = "EMPTY"
                        print(f"You picked up the key ({inventory["KEYBASIC"]} keys available)")
                        break

                    elif option == "no" or option == "n":
                        print("You leave the key on the ground")
                        break

                    else:
                        print("Invalid input (try yes or no)")

            if Room.get_room_type(self.x_pos, self.y_pos) == "KEYORNATEPICKUP":
                print()
                print("There is a ornate golden key on a small wooden pedestal in this room")
                while True:
                    option = input("Do you pick up the ornate key? - ")
                    if option == "yes" or option == "y":
                        inventory["KEYORNATE"] += 1
                        Room.get_room(self.x_pos, self.y_pos).room_type = "EMPTYPEDESTAL"
                        print(f"You picked up the ornate key ({inventory["KEYORNATE"]} keys available)")
                        break

                    elif option == "no" or option == "n":
                        print("You leave the ornate key on the pedestal")
                        break

                    else:
                        print("Invalid input (try yes or no)")

            if Room.get_room_type(self.x_pos, self.y_pos) == "SWORDPICKUP":
                print()
                print("There is a worn steel sword on a rack in this room")
                while True:
                    option = input("Do you take the sword? - ")
                    if option == "yes" or option == "y":
                        inventory["SWORD"] += 1
                        Room.get_room(self.x_pos, self.y_pos).room_type = "EMPTYRACK"
                        print(f"You took the sword ({inventory["SWORD"]} sword)")
                        break

                    elif option == "no" or option == "n":
                        print("You leave the sword on the rack")
                        break

                    else:
                        print("Invalid input (try yes or no)")

            if Room.get_room_type(self.x_pos, self.y_pos) == "SKELETONENCOUNTER":
                print()
                print("An armed reanimated skeleton attacks you when you enter this room")
                skeleton_max_health = 20
                skel_health = skeleton_max_health
                skel_damage = 4
                skel_staggered = False
                while True:
                    print("You can attack (a), defend (d), or flee (f)")
                    option = input("What action do you take against the skeleton? - ")
                    is_defending = False
                    if option == "attack" or option == "a":
                        turn_damage = 0
                        if inventory["SWORD"] > 0:
                            turn_damage = 3
                        else:
                            turn_damage = 1

                        if skel_staggered:
                            turn_damage *= 2.5
                            skel_staggered = False
                        skel_health -= turn_damage
                        print(f"Skeleton took {turn_damage} damage ({skel_health} / {skeleton_max_health})")
                        print("Skeleton regains its footing")

                    elif option == "defend" or option == "d":
                        is_defending = True
                        skel_staggered = True
                        print("You focus on defending yourself, you stagger it and it will deal less damage when it attacks you")
                    elif option == "flee" or option == "f":
                        print("Coward")
                        break
                    else:
                        print("Invalid input, please try again")

                    if is_defending:
                        inventory["HEALTH"] -= skel_damage / 2
                        print(f"You block and take {skel_damage / 2} damage from the skeleton ({inventory['HEALTH']} / {MAX_HEALTH} remaining)")
                    else:
                        inventory["HEALTH"] -= skel_damage
                        print(f"You take {skel_damage} damage from the skeleton ({inventory['HEALTH']} / {MAX_HEALTH} remaining)")

                    if skel_health <= 0:
                        inventory["FEMURBONE"] += 1
                        print(f"You defeat the skeleton and pickup femur bone ({inventory["FEMURBONE"]} femur bone(s))")
                        win_game()
                        break

                    if inventory["HEALTH"] <= 0:
                        lose_game()

                    print()
            
            if Room.get_room_type(self.x_pos, self.y_pos) == "EMPTY":
                print("There is nothing in this room")

            if Room.get_room_type(self.x_pos, self.y_pos) == "EMPTYPEDESTAL":
                print("There is an empty pedestal in this room")

            if Room.get_room_type(self.x_pos, self.y_pos) == "EMPTYRACK":
                print("There is an empty sword rack in this room")
    

        x_target = self.x_pos + x_delta
        y_target = self.y_pos + y_delta
        if Room.exists(self.x_pos + x_delta, self.y_pos + y_delta):
            query_wall_pos = (self.x_pos, self.y_pos, x_target, y_target)
            query_wall = Wall.check_for_wall(query_wall_pos)

            if not query_wall:
                print(f"Moved the player to the room at {self.x_pos + x_delta}, {self.y_pos + y_delta}")
                step(x_delta, y_delta)

            elif query_wall == "OPENDOOR":
                print(f"Player moved through an open door to the room at {self.x_pos + x_delta}, {self.y_pos + y_delta}")
                step(x_delta, y_delta)


            elif query_wall == "LOCKEDDOORBASIC":
                print("There is a locked door in the way of the player moving that way, try to unlock it or try a different direction")
                if inventory["KEYBASIC"] > 0:
                    while True:
                        option = input(f"Do you unlock it? ({inventory["KEYBASIC"]} keys available) - ")
                        if option == "yes" or option == "y":
                            wall = Wall.get_wall(query_wall_pos)
                            wall.wall_type = "OPENDOOR"
                            inventory["KEYBASIC"] -= 1
                            print(f"Player unlocked and moved through a door to {self.x_pos + x_delta}, {self.y_pos + y_delta}")
                            step(x_delta, y_delta)
                            break
                        elif option == "no" or option == "n":
                            print("The door stays locked")
                            break
                        else:
                            print("Invalid input (try yes or no)")

                elif inventory["KEYBASIC"] < 1:
                    print("You do not have a key to open this door")

            elif query_wall == "LOCKEDDOORORNATE":
                print("There is an ornate locked door in the way of the player moving that way, try to unlock it or try a different direction")
                if inventory["KEYORNATE"] > 0:
                    while True:
                        option = input(f"Do you unlock it? ({inventory["KEYORNATE"]} keys available) - ")
                        if option == "yes" or option == "y":
                            wall = Wall.get_wall(query_wall_pos)
                            wall.wall_type = "OPENDOOR"
                            inventory["KEYORNATE"] -= 1
                            print(f"Player unlocked and moved through a door to {self.x_pos + x_delta}, {self.y_pos + y_delta}")
                            step(x_delta, y_delta)
                            break
                        elif option == "no" or option == "n":
                            print("The ornate door stays locked")
                            break
                        else:
                            print("Invalid input (try yes or no)")

                elif inventory["KEYORNATE"] < 1:
                    print("You do not have a key to open this door")

            else:

                print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.x_pos}, {self.y_pos}")
        else:
            print(f"There is a wall in the way of the player moving that way, try a different direction, player stays at {self.x_pos}, {self.y_pos}")
    
player = Player(1, 1)

Room.generate_rooms(3, 3, 0, 0)
Room.set_room_type(2, 1, "KEYBASICPICKUP")
Room.set_room_type(0, 0, "KEYORNATEPICKUP")

Wall((1, 1, 2, 1), "SOLID")
Wall((1, 1, 0, 1), "OPENDOOR")
Wall((0, 1, 0 ,2), "SOLID")
Wall((1, 0, 0, 0), "SOLID")
Wall((0, 1, 0, 0), "LOCKEDDOORBASIC")

Room.generate_rooms(1, 1, 1, -1)
Room.set_room_type(1, -1, "SWORDPICKUP")

Room.generate_rooms(1, 2, 1, 3)
Room.set_room_type(1, 4, "SKELETONENCOUNTER")
Wall((1, 2, 1, 3), "LOCKEDDOORORNATE")



while True:
    choice_count += 1
    print(f">-----------------< Move {choice_count} >-----------------<")
    option = input("Where do you go? - ")

    if option == "forward" or option == "for" or option == "f" or option == "w":
        player.move(1, 0)
    elif option == "right" or option == "rit" or option == "r" or option == "d":
        player.move(0, 1)
    elif option == "backward" or option == "bac" or option == "b" or option == "s":
        player.move(-1, 0)
    elif option == "left" or option == "lef" or option == "l" or option == "a":
        player.move(0, -1)
    elif option == "query" or option == "qer" or option == "q":
        player.inventory_query()
        player.spatial_query()
    elif option == "whats going on im so lost":
        print("the red circle is at your spawn, forward moves you up, right moves you to the right")
        image.show()
    else:
        print("Invalid input (try forward, right, left, backward, query, or whats going on im so lost, or try inputing their first letters)")
    print()
