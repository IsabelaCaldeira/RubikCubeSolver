# Rubik Cube Solver :bulb:	

The rubik cube is a toy for kids and also a passion of the mathematicians. It is very complex and there are A LOT of possibilities when is about solving one.

(When I say a lot is I mean 43,252,003,274,489,856,000 possible combinations.)

By Default the solver will work with a randomly scrambled cube however this can be modified. To modify the cube being solved go into the main.py file and change the following variable to the representation of the cube you want.

```
cube = RubiksCube(
    state="rrrwrwrgryrywwwwrwbrbggggggwowyyyyyygygbbbbbbooobooooo"
)
```

You can also adjust your heuristics globals found at the top:

```
MAX_MOVES = 5 #max amount of moves when building heuristics map
NEW_HEURISTICS = False #control for overwritting heuristics
HEURISTIC_FILE = 'heuristic.json' #file that the heuristics are saved in or need to be saved in
```
# Launch Instructions
step 1: open your console <br>
step 2: create a virutal enviroment <br>
step 3: type the following command: <br>

```
pip install -r requirements.txt
```

step 4: type the following command:

```
cd <app directory>
```

step 5: type the following command:

```
python3 main.py
```

step 6: type in the action you wish to perform

