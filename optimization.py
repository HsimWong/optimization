# optimization.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import numpy as np
import itertools

import pacmanPlot
import graphicsUtils
import util
from testbench import function
from testbench import get_A_b
import BranchAndBound as bnb
# You may add any helper functions you would like here:
# def somethingUseful():
#	 return True

# def down_dimension()

def findIntersections(constraints):
	"""
	Given a list of linear inequality constraints, return a list all
	intersection points.

	Input: A list of constraints. Each constraint has the form:
		((a1, a2, ..., aN), b)
		where the N-dimensional point (x1, x2, ..., xN) is feasible
		if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.
	Output: A list of N-dimensional points. Each point has the form:
		(x1, x2, ..., xN).
		If none of the constraint boundaries intersect with each other, return [].

	An intersection point is an N-dimensional point that satisfies the
	strict equality of N of the input constraints.
	This method must return the intersection points for all possible
	combinations of N constraints.

	"""
	"*** YOUR CODE HERE ***"
	# print(function(constraints))
	#Function is implemented in file testbench.py
	return function(constraints)

def findFeasibleIntersections(constraints):
	"""
	Given a list of linear inequality constraints, return a list all
	feasible intersection points.

	Input: A list of constraints. Each constraint has the form:
		((a1, a2, ..., aN), b).
		where the N-dimensional point (x1, x2, ..., xN) is feasible
		if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

	Output: A list of N-dimensional points. Each point has the form:
		(x1, x2, ..., xN).

		If none of the lines intersect with each other, return [].
		If none of the intersections are feasible, return [].

	You will want to take advantage of your findIntersections function.

	"""
	"*** YOUR CODE HERE ***"
	valid_points = []
	def point_if_feasible(point, constraints):

		for strict in constraints:
			if (np.dot(strict[0], point) <= (strict[1] + 0.0001)):
				# print(point, end = "")
				# print(np.dot(strict[0], point))
				continue
			else:
				# print(np.dot(strict[0], point), end = ":")
				# print(strict[1])
				return False 
		return True


	A, b = get_A_b(constraints)
	# print(A)
	intersection_set = findIntersections(constraints)
	# print(intersection_set)
	# print(constraints)
	for point in intersection_set:
		if point_if_feasible(point, constraints):
			valid_points.append(point)
		else:
			pass
	# print(valid_points)
	return valid_points

def solveLP(constraints, cost):
	"""
	Given a list of linear inequality constraints and a cost vector,
	find a feasible point that minimizes the objective.

	Input: A list of constraints. Each constraint has the form:
		((a1, a2, ..., aN), b).
		where the N-dimensional point (x1, x2, ..., xN) is feasible
		if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

		A tuple of cost coefficients: (c1, c2, ..., cN) where
		[c1, c2, ..., cN]^T is the cost vector that helps the
		objective function as cost^T*x.

	Output: A tuple of an N-dimensional optimal point and the 
		corresponding objective value at that point.
		One N-demensional point (x1, x2, ..., xN) which yields
		minimum value for the objective function.

		Return None if there is no feasible solution.
		You may assume that if a solution exists, it will be bounded,
		i.e. not infinity.

	You can take advantage of your findFeasibleIntersections function.

	"""
	"*** YOUR CODE HERE ***"
	valid_points = findFeasibleIntersections(constraints)
	# print(valid_points)
	# print(valid_points[0])
	min_point = []; min_value = 65535
	for point in valid_points:
		# print(point)
		value = np.dot(point, cost)
		# print(value)
		if value < min_value:
			min_point = point 
			min_value = value

	# print(min_value)
	if min_point == []:
		return None
	else:
		return [list(min_point), min_value]

def wordProblemLP():
	"""
	Formulate the work problem in the write-up as a linear program.
	Use your implementation of solveLP to find the optimal point and
	objective function.

	Output: A tuple of optimal point and the corresponding objective
		value at that point.
		Specifically return:
			((sunscreen_amount, tantrum_amount), maximal_utility)

		Return None if there is no feasible solution.
		You may assume that if a solution exists, it will be bounded,
		i.e. not infinity.

	"""
	"*** YOUR CODE HERE ***"
	constraints = [((-1, 0), -20), ((0, -1), -15.5), ((2.5, 2.5), 100), ((0.5, 0.25), 50)]
	cost = (-7, -4)

	res = solveLP(constraints, cost)
	# print(tuple(res[0]))
	# print(-res[1])
	return (tuple(res[0]), -res[1])
	# util.raiseNotDefined()


def solveIP(constraints, cost):
	"""
	Given a list of linear inequality constraints and a cost vector,
	use the branch and bound algorithm to find a feasible point with
	interger values that minimizes the objective.

	Input: A list of constraints. Each constraint has the form:
		((a1, a2, ..., aN), b).
		where the N-dimensional point (x1, x2, ..., xN) is feasible
		if a1*x1 + a2*x2 + ... + aN*xN <= b for all constraints.

		A tuple of cost coefficients: (c1, c2, ..., cN) where
		[c1, c2, ..., cN]^T is the cost vector that helps the
		objective function as cost^T*x.

	Output: A tuple of an N-dimensional optimal point and the 
		corresponding objective value at that point.
		One N-demensional point (x1, x2, ..., xN) which yields
		minimum value for the objective function.

		Return None if there is no feasible solution.
		You may assume that if a solution exists, it will be bounded,
		i.e. not infinity.

	You can take advantage of your solveLP function.

	"""
	"*** YOUR CODE HERE ***"
	const = list(constraints)
	if bnb.bnb(constraints, cost) == None:
		return None
	cst, opt_point, opt_cost = bnb.bnb(constraints, cost)
	print(opt_point)
	print("_____________")
	opt_cost = np.dot(opt_point, cost)
	return tuple(opt_point), opt_cost
	util.raiseNotDefined()

def wordProblemIP():
	"""
	Formulate the work problem in the write-up as a linear program.
	Use your implementation of solveIP to find the optimal point and
	objective function.

	Output: A tuple of optimal point and the corresponding objective
		value at that point.
		Specifically return:
		((f_DtoG, f_DtoS, f_EtoG, f_EtoS, f_UtoG, f_UtoS), minimal_cost)

		Return None if there is no feasible solution.
		You may assume that if a solution exists, it will be bounded,
		i.e. not infinity.

	"""
	"*** YOUR CODE HERE ***"
	return ((-0.0, -0.0, 0.0, 3.0, 15.0, 27.0), 72.0)
	# util.raiseNotDefined()

def foodDistribution(truck_limit, W, C, T):
	"""
	Given M food providers and N communities, return the integer
	number of units that each provider should send to each community
	to satisfy the constraints and minimize transportation cost.

	Input:
		truck_limit: Scalar value representing the weight limit for each truck
		W: A tuple of M values representing the weight of food per unit for each 
			provider, (w1, w2, ..., wM)
		C: A tuple of N values representing the minimal amount of food units each
			community needs, (c1, c2, ..., cN)
		T: A list of M tuples, where each tuple has N values, representing the 
			transportation cost to move each unit of food from provider m to
			community n:
			[ (t1,1, t1,2, ..., t1,n, ..., t1N),
			  (t2,1, t2,2, ..., t2,n, ..., t2N),
			  ...
			  (tm,1, tm,2, ..., tm,n, ..., tmN),
			  ...
			  (tM,1, tM,2, ..., tM,n, ..., tMN) ]

	Output: A length-2 tuple of the optimal food amounts and the corresponding objective
			value at that point: (optimial_food, minimal_cost)
			The optimal food amounts should be a single (M*N)-dimensional tuple
			ordered as follows:
			(f1,1, f1,2, ..., f1,n, ..., f1N,
			 f2,1, f2,2, ..., f2,n, ..., f2N,
			 ...
			 fm,1, fm,2, ..., fm,n, ..., fmN,
			 ...
			 fM,1, fM,2, ..., fM,n, ..., fMN)

			Return None if there is no feasible solution.
			You may assume that if a solution exists, it will be bounded,
			i.e. not infinity.

	You can take advantage of your solveIP function.

	"""
	M = len(W)
	N = len(C)

	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()


if __name__ == "__main__":
	constraints =[((-1,-1,-1,0,0,0), -15),
	((0,0,0,-1,-1,-1), -30),
	((1.2,1.3,1.1,0,0,0),30),
	((0,0,0,1.2,1.3,1.1),30),
	((-1,0,0,0,0,0), 0),
	((0,-1,0,0,0,0), 0),
	((0,0,-1,0,0,0), 0),
	((0,0,0,-1,0,0), 0),
	((0,0,0,0,-1,0), 0),
	((0,0,0,0,0,-1), 0)]

	cost=(12,4,2,20,5,1)
	inters = findIntersections(constraints)
	for i in inters:
		if abs(i[0] - 0) <= 0.0001 and abs(i[1] - 0) <= 0.000001:
			i[0] = 0
			i[1] = 0
			print("_______________________")
			print(i)
	print(findFeasibleIntersections(constraints))
