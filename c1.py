
from select import select


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
        if color == "B":
            self.blue_balls -= 1
            self.trigger(3, 0, color, 1)
        elif color == "R":
            self.red_balls -= 1
            self.trigger(7, 0, color, -1)
        else:
            self.blue_balls -= 1
            self.trigger(3, 0, "B", 1)


    def trigger(self, x, y, color, dir):
        if x < 0 or x > 10:
            print("halt")
        if y > 9 and x != 5:
            if x < 5:
                print("drop blue")
                self.output += color
                self.drop_ball("B")
            elif x >= 5:
                print("drop red")
                self.output += color
                self.drop_ball("R")
        elif self.board[y][x] == "L":
            print("L", x, y)
            self.board[y][x] = "R"
            self.trigger(x-1, y+1, color, -1)
        elif self.board[y][x] == "R":
            print("R", x, y)
            self.board[y][x] = "L"
            self.trigger(x+1, y+1, color, 1)
        elif self.board[y][x] == ">":
            print(">", x, y)
            self.trigger(x+1, y+1, color, 1)
        elif self.board[y][x] == "<":
            print("<", x, y)
            self.trigger(x-1, y+1, color, -1)
        elif self.board[y][x] == "X":
            print("X", x, y)
            self.trigger(x+dir, y+1, color, dir)
        elif self.board[y][x] == "/":
            print("/", x, y)
            self.board[y][x] = "\\"
            self.trigger(x-1, y+1, color, -1)
        elif self.board[y][x] == "\\":
            print("\\", x, y)
            self.board[y][x] = "/"
            self.trigger(x+1, y+1, color, 1)
        else:
            print(f"{self.board[y][x]}, {x}, {y}")
    
    def update_aj_gears(x, y):
        pass
            


f = Field()

f.print_field()
print()
f.read_input()
print()
f.print_field()
f.drop_ball("B")
f.print_field()