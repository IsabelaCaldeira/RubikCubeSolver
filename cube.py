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
        