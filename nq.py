""" CMSC471 01 hw3 spring 2016
	Dean Fleming, deanf1@umbc.edu

	A subclass of a constraint problem to solve an n-queens problem of
	a given size with a given solver """

from constraint import *

class NQ(Problem):

	def __init__(self, n=8, solver=None):

		""" N is the size of the board, solver is the CSP solver
			that will be used to sove the problem """

		# call the base class init method
		super(NQ, self).__init__(solver=solver)

		# set any NQ instance variables needed

		# define CSP variables with their domains
		self.addVariables(range(n), range(n))

		# add CSP constraints
		self.addConstraint(AllDifferentConstraint(), range(n))
		for i in range(n):	
			for j in range(n):
				if i < j:
					self.addConstraint(lambda x, y, i = i, j = j: 
						abs(x - y) != abs(i - j) and x != y, (i, j))