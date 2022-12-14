import sys
sys.path.append("../src")
from automata import run
from rules import rules
from starters import random_cells

run(
    cells = random_cells(100, 100, p_life=0.5),
    rules = rules["Move"],
    boundaries = "periodic",
    nsteps = 100,
    print_steps = True,
    live_view = True,
    data_output = "./move.out",
    anim_output = "./move.gif"
)