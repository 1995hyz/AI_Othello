import board


class Human:

    def __init__(self, color, name):
        self.type = "human"
        self.color = color
        self.name = name

    def get_coordination(self, available_move):
        while True:
            try:
                row = int(input("Enter row of move (0-7): "))
                column = int(input("Enter column of move (0-7): "))
                if (row, column) in available_move:
                    return [0, row, column]
                else:
                    print("(" + str(row) + ", " + str(column) + ") is not a legal move." )
            except ValueError as e:
                print(e)
