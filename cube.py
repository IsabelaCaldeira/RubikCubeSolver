from random import randint, choice

class RubiksCube:
    """
    Class containing the rubiks cube code
    """

    def __init__(
        self,
        n = 3,
        colours = ['w', 'o', 'g', 'r', 'b', 'y'],
        state = None
    ):
        
        """"
        Input: n - integer representing the width and height of the rubiks cube
               colours - list containing the first letter of ever colour you wish to use (Default = ['w', 'o', 'g', 'r', 'b', 'y']) [OPTIONAL]
               state - string representing the current state of the rubix cube (Default = None) [OPTIONAL]
        Description: Initialize the rubiks cube
        Output: None
        """
        if state is None:
            self.n = n
            self.colours = colours
            self.reset()
        else:
            self.n = int((len(state) / 6) ** (.5))
            self.colours = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.colours: self.colours.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) - 1:
                    self.cube.append([[]])