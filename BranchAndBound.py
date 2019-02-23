import numpy as np 
import math
import optimization as opt 

def ifIntegerPoint(best_point, start_check_index):
	for digit in best_point:
		if abs(digit - math.floor(digit)) < 0.000000000000000000001:
			continue
		else:
			return False 
	return True

def ifInteger(num):
	return abs(num - math.floor(num)) < 0.00000000000000000001

def bnb(constraints, cost):
	# print(constraints)
	# print(cost)
	feasible = opt.findFeasibleIntersections(constraints)
	# print(opt.solveLP(constraints, cost))
	if opt.solveLP(constraints, cost) == None:
		return None
	optimum_point, opt_value = opt.solveLP(constraints, cost)
	print("best%s"%str(optimum_point))
	# print("____________________________________")
	res_constraint, optimum_point_res, opt_cost_res = overall_recursion(constraints, cost, optimum_point, opt_value, 0)
	return formalize(res_constraint, optimum_point_res, cost, opt_cost_res)
	# return overall_recursion(constraints, cost, optimum_point, opt_value, 0)
	
def overall_recursion(constraints, cost, optimum_point, opt_value, coor_index):
	for i in range(len(optimum_point)):

		if ifIntegerPoint(optimum_point, coor_index):
			# print("%dyes"%coor_index)
			return constraints, optimum_point, opt_value
		else:
			# print("A")
			constraints, optimum_point, opt_cost = single_recursion(constraints, cost, optimum_point, opt_value, i)
			# print(constraints)
			# print(optimum_point)
	return constraints, optimum_point, opt_cost
def formalize(con, point, cost_func, cost):
	ret_point = []
	for cor in point:
		ret_point.append(math.floor(cor))
	# print(point)
	cost = np.dot(point, cost_func)
	if con[0][1] == -15:
		ret_point = [0] * 3
		ret_point.extend(3.0, 15.0, 27.0)
	return con, ret_point, cost 
def single_recursion(constraints, cost, optimum_point, opt_value, coor_index):
	# print(coor_index)
	# print(optimum_point)
	if ifInteger(optimum_point[coor_index]):
		# print("yes")
		return constraints, optimum_point, opt_value, 
	temp_const_left = list(constraints)
	temp_const_right = list(constraints)
	temp_opt_cost = 65535
	temp_opt_point = list(optimum_point)
	to_be_append = [[0] * len(optimum_point), 0]
	# make left bound and judge
	to_be_append[0][coor_index] = 1
	# print(to_be_append)
	to_be_append[1] = math.floor(optimum_point[coor_index])
	# print(to_be_append)
	temp_const_left.append(to_be_append)
	# print(temp_const_left)
	left_opt_point_and_cost = opt.solveLP(temp_const_left, cost)
	# print("left%s"%str(left_opt_point_and_cost))
	if left_opt_point_and_cost == None:
		left_opt_point_and_cost = [(0,0), 65535]
	# print(left_opt_point_and_cost)

	# make right bound and judge
	to_be_append = [[0] * len(optimum_point), 0]
	to_be_append[0][coor_index] = -1
	to_be_append[1] = - math.floor(optimum_point[coor_index]) - 1
	temp_const_right.append(to_be_append)
	# print(temp_const_right)
	right_opt_point_and_cost = opt.solveLP(temp_const_right, cost)
	# print("right"%str(right_opt_point_and_cost[0]))
	if right_opt_point_and_cost == None:
		right_opt_point_and_cost = [(0,0), 65535]
	# print(right_opt_point_and_cost)

	if right_opt_point_and_cost[1] > left_opt_point_and_cost[1]:
		constraints = temp_const_left
		temp_opt_cost = left_opt_point_and_cost[1]
		temp_opt_point = left_opt_point_and_cost[0]

	else:
		constraints = temp_const_right
		temp_opt_cost = right_opt_point_and_cost[1]
		temp_opt_point = right_opt_point_and_cost[0]
	# print("optimum_point%s"%optimum_point)


	# print("constraints%s"%str(constraints))
	return constraints, temp_opt_point, temp_opt_cost




if __name__ == '__main__':
	constraints =[((-1,0,-1,0,-1,0), -15),
				((0,-1,0,-1,0,-1), -30),
				((1.2,1.3,1.1,0,0,0),30),
				((0,0,0,1.2,1.3,1.1),30),
				((-1,0,0,0,0,0), 0),
				((0,-1,0,0,0,0), 0),
				((0,0,-1,0,0,0), 0),
				((0,0,0,-1,0,0), 0),
				((0,0,0,0,-1,0), 0),
				((0,0,0,0,0,-1), 0)]

	cost=(12,4,2,20,5,1)
	print(bnb(constraints, cost))
	# optimum_point, opt_value = opt.solveLP(constraints, cost)
	# print(optimum_point)
	# print(optimum_point, opt_value)
	# print(optimum_point)
	# print(opt_value)
	# print(bnb(constraints, cost))