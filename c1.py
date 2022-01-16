


class Pin:
    def __init__(self, x, y):
        self.pos = [x, y]
    
    def update(self):
        pass


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
        self.output = []

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


    def drop_ball(color):
        if color == "B":
            self.trigger(0, 3, color, 1)
        elif color == "R":
            self.trigger(0, 7, color, -1)
        else:
            self.trigger(0, 3, "B", 1)


    def trigger(x, y, color, dir):
        if y > 10:
            pass
            


f = Field()

f.print_field()
print()
f.read_input()
print()
f.print_field()