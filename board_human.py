import board


class Human:

    def __init__(self):
        name = "human"

    @staticmethod
    def get_coordination():
        while True:
            try:
                row = int(input("Enter row of move (0-7): "))
                column = int(input("Enter column of move (0-7): "))
                return [0, row, column]
            except ValueError as e:
                print(e)
