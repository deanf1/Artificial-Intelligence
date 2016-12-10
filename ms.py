""" CMSC471 01 hw3 spring 2016
	Dean Fleming, deanf1@umbc.edu

	A subclass of a constraint problem to find a magic square for a
	nxn grid and sum n*(n*n+1)/2. """

from constraint import *

class MS(Problem):

	def __init__(self, n=3, solver=None):

		""" N is the size of the magic square, solver is the CSP solver
			that will be used to sove the problem """

		# call the base class init method
		super(MS, self).__init__(solver=solver)

		# set any MS instance variables needed
		magicSum = n * (n**2 + 1) / 2
		lToRDiagonal = []
		rToLDiagonal = []
		for i in range(n):
			lToRDiagonal.append((n + 1) * i)
			rToLDiagonal.append((n - 1) * (i + 1))

		# define CSP variables with their domains
		self.addVariables(range(n**2), range(1, n**2 + 1))

		# add CSP constraints 
		self.addConstraint(AllDifferentConstraint(), range(n**2))
		self.addConstraint(ExactSumConstraint(magicSum), lToRDiagonal)
		self.addConstraint(ExactSumConstraint(magicSum), rToLDiagonal)
		for row in range(n):
			self.addConstraint(ExactSumConstraint(magicSum), 
				[row * n + i for i in range(n)])
		for col in range(n):
			self.addConstraint(ExactSumConstraint(magicSum), 
				[col + n * i for i in range(n)])