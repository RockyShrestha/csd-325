# Rakesh Shrestha
# Date: July 19, 2026
# Group-A: Rakesh Shrestha, Brandon Cox, Jerrold Icban, Christian Thompson
# CSD325-T301 Advanced Python - Module 6.2 Assignment
#
# Purpose: Forest fire simulation with an added lake/water feature that
# acts as a permanent firebreak in the middle of the forest.
#
# Original program "Forest Fire Sim" by Al Sweigart, modified by Sue Sampson
# (instructor version distributed in Module 5). Water/lake feature added by
# Group-A for Module 6.2.

# A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
# Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
# ** use spaces, not indentation to modify **
# Tags: short, bext, simulation

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New for Module 6: the lake/firebreak character.

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

# New for Module 6: how big the lake is, measured out from the center point
# in the x and y directions (this is the ellipse "radius" in each direction).
LAKE_WIDTH_RADIUS = 6
LAKE_HEIGHT_RADIUS = 3


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if forest[(x, y)] == WATER:
                    # water never changes, just copy it over
                    nextForest[(x, y)] = WATER
                elif ((forest[(x, y)] == EMPTY)
                      and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # only spreads to trees, so water blocks it
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a new forest data structure, now with a lake added
    near the center of the grid."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    addLake(forest)  # New for Module 6: carve the lake into the forest.
    return forest


def addLake(forest):
    """New for Module 6 - adds a lake near the center so fire can't
    cross it. Called after the forest grid is built, so the lake
    overwrites any trees that were already there.

    Used the center point (width // 2, height // 2) like we saw in
    the Mod5 Cartesian video, then checked each cell against an
    ellipse formula to see if it falls inside the lake shape.
    """
    centerX = forest['width'] // 2
    centerY = forest['height'] // 2

    for x in range(forest['width']):
        for y in range(forest['height']):
            deltaX = x - centerX
            deltaY = y - centerY
            # Standard ellipse formula (deltaX/rx)^2 + (deltaY/ry)^2 <= 1
            # marks every cell that falls inside the oval-shaped lake.
            if ((deltaX * deltaX) / (LAKE_WIDTH_RADIUS ** 2)
                    + (deltaY * deltaY) / (LAKE_HEIGHT_RADIUS ** 2)) <= 1:
                forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                # New for Module 6: draw the lake in blue.
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the simulation:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
