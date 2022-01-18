


class Field:
    def __init__(self):
        self.board = [
            [' ', ' ', '.', ',', '.', ' ', '.', ',', '.', ' ', ' '],
            [' ', '.', ',', '.', ',', '.', ',', '.', ',', '.', ' '],
            ['.', ',', '.', ',', '.', ',', '.', ',', '.', ',', '.'],
            [',', '.', ',', '.', ',', '.', ',', '.', ',', '.', ','],
            ['.', ',', '.', ',', '.', ',', '.', ',', '.', ',', '.'],
            [',', '.', ',', '.', ',', '.', ',', '.', ',', '.', ','],
            ['.', ',', '.', ',', '.', ',', '.', ',', '.', ',', '.'],
            [',', '.', ',', '.', ',', '.', ',', '.', ',', '.', ','],
            ['.', ',', '.', ',', '.', ',', '.', ',', '.', ',', '.'],
            [',', '.', ',', '.', ',', '.', ',', '.', ',', '.', ','],
            [' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ']
        ]
        
        self.start_ball = "B"
        self.blue_balls = 5
        self.red_balls = 5
        self.output = ""

    def read_input(self):
        inp = input().split(" ")
        self.start_ball = inp[0]
        self.blue_balls = int(inp[1])
        self.red_balls = int(inp[2])
        for i in range(11):
            inp = list(input())
            for j in range(len(inp)):
                if i == 0:
                    self.board[i][j+2] = inp[j]
                elif i == 1:
                    self.board[i][j+1] = inp[j]
                elif i == 10:
                    self.board[i][j+5] = inp[j]
                else:
                    self.board[i][j] = inp[j]


    def print_field(self):
        print(f"B:{self.blue_balls}, R:{self.red_balls}, S:{self.start_ball}, OUT:{self.output}")
        for i in range(len(self.board)):
            line = ""
            for j in range(len(self.board[i])):
                line += self.board[i][j]
            print(line)


    def drop_ball(self, color):
        trigger = None
        if color == "B":
            self.blue_balls -= 1
            if self.blue_balls >= 0:
                trigger = self.trigger(3, 0, color, 1)
        elif color == "R":
            self.red_balls -= 1
            if self.red_balls >= 0:
                trigger = self.trigger(7, 0, color, -1)
        else:
            self.blue_balls -= 1
            if self.blue_balls >= 0:
                trigger = self.trigger(3, 0, "B", 1)
        return trigger



    def trigger(self, x, y, color, dir):
        trigger = None
        if x < 0 or x > 10:
            # print("halt")
            pass
        if y > 9 and x != 5:
            if x < 5:
                # print("drop blue")
                self.output += color
                trigger = self.drop_ball("B")
            elif x >= 5:
                # print("drop red")
                self.output += color
                trigger = self.drop_ball("R")
        elif self.board[y][x] == "L":
            # print("L", x, y)
            self.board[y][x] = "R"
            trigger = (x-1, y+1, color, -1)
        elif self.board[y][x] == "R":
            # print("R", x, y)
            self.board[y][x] = "L"
            trigger = (x+1, y+1, color, 1)
        elif self.board[y][x] == ">":
            # print(">", x, y)
            trigger = (x+1, y+1, color, 1)
        elif self.board[y][x] == "<":
            # print("<", x, y)
            trigger = (x-1, y+1, color, -1)
        elif self.board[y][x] == "X":
            # print("X", x, y)
            trigger = (x+dir, y+1, color, dir)
        elif self.board[y][x] == "/":
            # print("/", x, y)
            # self.board[y][x] = "\\"
            self.update_aj_gears(x, y)
            self.clear_bs()
            trigger = (x-1, y+1, color, -1)
        elif self.board[y][x] == "\\":
            # print("\\", x, y)
            # self.board[y][x] = "/"
            self.update_aj_gears(x, y)
            self.clear_bs()
            trigger = (x+1, y+1, color, 1)
        else:
            # print(f"{self.board[y][x]}, {x}, {y}")
            pass
        
        return trigger
    

    def update_aj_gears(self, x, y):
        if self.board[y][x] == "o" or self.board[y][x] == "\\" or self.board[y][x] == "/": 
            if self.board[y][x] == "\\":
                self.board[y][x] = "/"
            elif self.board[y][x] == "/":
                self.board[y][x] = "\\"
            self.board[y][x] += "b"
            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for d in dirs:
                if x+d[0] > -1 and x+d[0] < 10 and y+d[1] > -1 and y+d[1] < 10:
                    self.update_aj_gears(x+d[0], y+d[1])



    def clear_bs(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if "b" in self.board[y][x]:
                    self.board[y][x] = self.board[y][x][:-1]

                    
            


f = Field()

# f.print_field()
# print()


f.read_input()

t = f.drop_ball(f.start_ball)
# print(t)
halt = False
while not halt:
    t = f.trigger(t[0], t[1], t[2], t[3])
    if t == None:
        halt = True


print(f.output)

# f.update_aj_gears(3, 0)
# f.clear_bs()

# f.print_field()

# f.update_aj_gears(2, 1)
# f.clear_bs()

# f.print_field()