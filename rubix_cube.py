class cube():
    def __init__(self, state="solved") -> list:
        if state == "solved":
            self.state = [
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
    [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
    [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
    [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
]
        else:
            self.state = state
    def updateState(cube):
        self.state = cube

class move(cube):
    def __init__(self, cube) -> None:
        pass
    def moveFrontTopLeft(cube):
        state = cube.state
        movers = [[[state[2][0][2], state[0][0][1], state[0][0][2]], [state[2][1][2], state[0][1][1], state[0][1][2]], [state[2][2][2], state[0][2][1], state[0][2][2]]], [[state[1][0][0], state[1][0][1], state[1][0][2]], [state[1][1][0], state[1][1][1], state[1][1][2]], [state[1][2][0], state[1][2][1], state[1][2][2]]], [[state[2][0][0], state[2][0][1], state[5][2][2]], [state[2][1][0], state[2][1][1], state[5][2][1]], [state[2][2][0], state[2][2][1], state[5][2][0]]], [[state[3][0][2], state[0][0][1], state[0][0][2]], [state[3][1][2], state[0][1][1], state[0][1][2]], [state[3][2][2], state[0][2][1], state[0][2][2]]], [[state[0][0][2], state[4][0][1], state[4][0][2]], [state[0][0][1], state[4][1][1], state[4][1][2]], [state[0][0][0], state[4][2][1], state[4][2][2]]], []]
        newState = None