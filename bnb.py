import optimization as opt 
import numpy as np 
def get_max_val_pnt(feasible, cost):
	max_val = -65535; max_point = feasible[0]
	for point in feasible:
		point_val = np.dot(point, cost)
		if point_val < max_val:
			max_point = point
			max_val = point_val
	return max_val, max_point

def ifIntegerPoint(best_point, start_check_index):
	for i in range(len(best_point)-start_check_index):
		if abs(best_point[i+start_check_index] - int(best_point[i]+start_check_index)) < 0.0000001:
			continue
		else:
			return False 
	return True

def ifCorOK(constraint, )

def branch_cut(constraint, mani_coor_ind, best_point):
	'''
	In this branch_cut function, left == 'l', right = 'r'
	'''
	cons_mani_value = constraint[-1][0][mani_coor_ind]
	# print(cons_mani_value)
	left_const = constraints
	right_const = constraints

	left_const[-1][mani_coor_ind] = int(cons_mani_value)
	right_const[-1][mani_coor_ind] = int(cons_mani_value) + 1
	return left_const, right_const
	


def rec_IP(constraints, cost, worst_point, worst_val, best_point, best_val, curr_chk_coor_ind):
	
	'''
	This function is for continuous recursion, which returns the best point with both value of integer.
	
	'''
	if ifIntegerPoint(best_point, curr_chk_coor_ind):
		return best_point, best_val
	else:
		'''
		separate: separate the flow into two branches: upper bound and bottom bound
		the bound strict is preliminarily dealt and locates at the back of the constraints
		'''
		constraints_left, constraints_right = branch_cut(constraints, curr_chk_coor_ind, best_point)


def bnb(constraints, cost):
	feasible = opt.findFeasibleIntersections(constraints)
	optimum_point, opt_value = opt.solveLP(constraints, cost)
	if ifIntegerPoint(optimum_point, 0):
		return optimum_point, opt_value
	else:
		worst_val, worst_point = get_max_val_pnt(feasible, cost)
		constraints.append([list(constraints[0][0]), constraints[0][1]]) # This element is for limit management in branch and bound process
		# Initialization
		for i in range(len(constraints[-1][0])):
			constraints[-1][0][i] = 0
		constraints[-1][1] = 0
		print(constraints[-1])
		return constraints, optimum_point
		# int_val, int_point = rec_IP(constraints, cost, worst_point, worst_val, best_point, best_val, 0)
		# return int_point, int_val

if __name__ == '__main__':
	constraints = [((-1, 0), -20), ((0, -1), -15.5), ((2.5, 2.5), 100), ((0.5, 0.25), 50)]
	cost = (2, 6)
	constraints, best_point = (bnb(constraints, cost))
	print(constraints)
	branch_cut(constraints, 0, best_point)
	print(constraints)
	# print(ifIntegerPoint(cost, 0))
	# print(bnb(constraints, cost))
	# print(check_integer(6.00))

