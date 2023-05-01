import json 
import os.path

from cube import RubiksCube
from solver import IDA_star, build_heuristic_db

MAX_MOVES = 5
NEW_HEURISTICS = False
HEURISTIC_FILE = 'heuristic.json'

#--------------------------------
cube = RubiksCube(n=3)
cube.show()
print('-----------')
#--------------------------------

if os.path.exists(HEURISTIC_FILE):
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)
else:
    h_db = None

if h_db is None or NEW_HEURISTICS is True:
    actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]
    h_db = build_heuristic_db(
        cube.stringify(),
        actions,
        max_moves = MAX_MOVES,
        heuristic = h_db
    )

    with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            h_db,
            f,
            ensure_ascii=False,
            indent=4
        )