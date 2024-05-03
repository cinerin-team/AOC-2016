class Day1:
    direction = None
    x = None
    y = None
    arr = []
    dists = set()

    def go2(self, dir, dis):
        if dir == "R":
            if self.direction == "N":
                self.direction = "E"
                for i in range(dis):
                    self.x += 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "E":
                self.direction = "S"
                for i in range(dis):
                    self.y -= 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "S":
                self.direction = "W"
                for i in range(dis):
                    self.x -= 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "W":
                self.direction = "N"
                for i in range(dis):
                    self.y += 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
        else:
            if self.direction == "N":
                self.direction = "W"
                for i in range(dis):
                    self.x -= 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "E":
                self.direction = "N"
                for i in range(dis):
                    self.y += 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "S":
                self.direction = "E"
                for i in range(dis):
                    self.x += 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True
            if self.direction == "W":
                self.direction = "S"
                for i in range(dis):
                    self.y -= 1
                    if (self.dists.__contains__(str(self.x) + "," + str(self.y))):
                        return False
                    else:
                        self.dists.add(str(self.x) + "," + str(self.y))
                return True

    def go(self, dir, dis):
        if dir == "R":
            if self.direction == "N":
                self.direction = "E"
                self.x += dis
                return
            if self.direction == "E":
                self.direction = "S"
                self.y -= dis
                return
            if self.direction == "S":
                self.direction = "W"
                self.x -= dis
                return
            if self.direction == "W":
                self.direction = "N"
                self.y += dis
                return
        else:
            if self.direction == "N":
                self.direction = "W"
                self.x -= dis
                return
            if self.direction == "E":
                self.direction = "N"
                self.y += dis
                return
            if self.direction == "S":
                self.direction = "E"
                self.x += dis
                return
            if self.direction == "W":
                self.direction = "S"
                self.y -= dis
                return

    def __init__(self, file):
        self.direction = 'N'
        self.x = 0
        self.y = 0
        self.dists.add("0,0")
        with open(file, "r") as f:
            line = f.readline()
            self.arr = line.split(", ")

    def task1(self):
        self.direction = 'N'
        self.x = 0
        self.y = 0
        for item in self.arr:
            self.go(item[:1], int(item[1:].strip()))

        return str(abs(self.x) + abs(self.y))

    def task2(self):
        self.direction = 'N'
        self.x = 0
        self.y = 0
        self.dists.clear()
        self.dists.add("0,0")
        for item in self.arr:
            if not (self.go2(item[:1], int(item[1:].strip()))):
                break

        return str(abs(self.x) + abs(self.y))
