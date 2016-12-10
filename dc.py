""" CMSC471 02 hw2 spring 2016
    Dean Fleming, deanf1@umbc.edu

    Homework 2
    Converts two three-letter words from one to the other by switching one
    letter at a time, each step in between being real words.
"""    

import aima.search as a       # AIMA module for search problems

dict_file = "words34.txt"
dictionary = {}

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SCRABBLE = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,
'j':6, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 
'u':1, 'v':4, 'w':4, 'x':6, 'y':4, 'z':10}

# parses words file
for line in open(dict_file):
    word, n = line.strip().split('\t')
    dictionary[word] = float(n)

class DC(a.Problem):

    """ Constructor """
    def __init__(self, initial='dog', goal='cat', cost='steps'):
        self.initial = initial
        self.goal = goal
        self.cost = cost

    """ Returns a possible letter swap as a tuple, the first item being the
    index of the swap, and the second item being the letter to swap to. """
    def actions(self, state):
        state = state.lower()
        stateList = list(state)

        # loops through letters in word
        for i in range(0, len(state)):
            oldLetter = stateList[i]    # saves last word for later
            
            # loops through alphabet, returns if valid word found
            for letter in ALPHABET:
                stateList[i] = letter 
                if "".join(stateList) in dictionary:
                    yield (i, letter)
            stateList[i] = oldLetter

    """ Returns the result of performing the action on the state """
    def result(self, state, action):
        stateList = list(state)
        stateList[action[0]] = action[1]
        return "".join(stateList)

    """ Checks to see if the goal is met """
    def goal_test(self, state):
        return state == self.goal

    """ Calculates the cost of various actions in various ways """
    def path_cost(self, c, state1, action, state2):
        if self.cost == "steps":
            return c + 1
        elif self.cost == "scrabble":
            return c + SCRABBLE[action[1]]
        elif self.cost == "frequency":
            return c + 1 + dictionary[state2]

    """ returns a string to represent a dc problem """
    def __repr__(self):
        return "Initial: %s, Goal: %s, Cost: %s" % self.initial, self.goal, 
        self.cost

    """ Heuristic: returns an estimate of the cost to get from the
    state of this node to the goal state.  The heuristic's value
    should depend on the Problem's cost parameter (steps, scrabble
    or frequency) as this will effect the estimate cost to get to
    the nearest goal. """
    def h(self, node):

        # For steps, count letters different in state and goal
        if self.cost == "steps":
            count = 0
            for i in range(0, len(node.state)):
                if node.state[i] != self.goal[i]:
                    ++count
            return count

        # For Scrabble, returns the difference in cost from state and goal
        elif self.cost == "scrabble":
            stateCost = 0
            goalCost = 0
            for i in range(0, len(node.state)):
                stateCost += SCRABBLE[node.state[i]]
            for i in range(0, len(self.goal)):
                goalCost += SCRABBLE[self.goal[i]]
            return abs(stateCost - goalCost) 

        # For frequency, returns the smallest cost in the path up to state
        elif self.cost == "frequency":
            cost = 1000000000000
            pathList = node.path()
            for i in range (0, len(pathList)):
                if dictionary[pathList[i].state] < cost:
                    cost = dictionary[pathList[i].state]
            return cost