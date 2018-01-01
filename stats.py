############################################
# Project: MCT-TFE
# File: stats.py
# By: ProgrammingIncluded
# Website: ProgrammingIncluded.com
############################################

from TFE import *
from MCT import *
from mct_config import *
import time
import traceback

TRIALS = 100

def main():
    games = []
    wins = 0

    for t in range(0, TRIALS):
        print "GAME: " + str(len(games) + 1)

        tfe = TFE()
        # generate a new
        tfe.putNew()
        tfe.putNew()

        mct = MCT()
        while (not tfe.isWin()) and (not tfe.isLose()):
            act = mct.run(tfe, MONTE_CARLO_RUN, True)

            # move grid
            tfe.moveGrid(act)

            # generate a new
            tfe.putNew()

        if tfe.isWin():
            games.append(1)
            wins += 1
        else:
            games.append(0)

        with open("stat_output.txt", "a") as f:
            f.write(str(games[-1]) + "\n")
        
        print float(wins) / len(games)



if __name__ == '__main__':
    main()