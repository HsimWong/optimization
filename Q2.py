import numpy as np
def point_if_feasible(point, constraints):
	for strict in constraints:
		# print(point)
		print(strict)
		if (np.dot(strict[0], point) <= strict[1]):
			print("pass")
			continue
		else:
			print("fail")
			return False 
	return True

if __name__ == '__main__':
	constraints = [ ((1, 1), 10),\
  ((-1, 0), 0),\
  ((0, -1), 0) ]
	point_if_feasible([0, 10], constraints)