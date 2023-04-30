from random import choice
from tqdm import tqdm

from cube import RubiksCube

class IDA_star(object):
    def __init__(self, heuristic, max_depth = 20):
        """
        Input: heuristic - dictionary representing the heuristic pre computed map
               max_depth - integer representing the max depth you want your game tree to reach (default = 20) [OPTIONAL]
        Description: Initialize the solver
        Output: None
        """
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []
    
    def run(self, state):
        """
        Input: state - string representing the current state of the cube
        Description: solve the rubix cube
        Output: list containing the moves taken to solve the cube
        """
        while True:
            status = self.search(state, 1)
            if status: return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

