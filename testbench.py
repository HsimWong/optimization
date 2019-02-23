import numpy as np 


def get_A_b(package):
	A = []; b = []; 
	# print( package)
	for line in package:
		# print(line[0])
		A.append(list(line[0]))

		b.append(line[1])
	return A, b

def find_one_intersection(package):
	A,b = get_A_b(package)
	# print(np.array(A).shape)
	if np.linalg.matrix_rank(A) == len(A[0]):
		result = (np.linalg.solve(A, b))
		return list(result)
	else:
		return -1
		# print(result)
	# print(package)
	# return list(result)

def function(constraints):
	packages = get_packages(constraints)
	# print(packages)
	inter_points = []
	for package in packages:
		# print(package)
		res = find_one_intersection(package)
		# print (res)
		# print(res)
		if not (res) == -1:
			inter_points.append(res)
	# print("Yes")
	# print(inter_points)
	return inter_points

def append_package(constraints, index_ptr):
	ret_array = []
	for index in index_ptr:
		ret_array.append(constraints[index])
	return ret_array

def get_packages(constraints):
	# Make packages index
	index_pointers = []; packages = []
	for index in range(2 ** len(constraints)):
		bin_str = bin(index)[2:].zfill(len(constraints))
		ptr = []
		for dig in bin_str:
			ptr.append(int(dig))
		if sum(ptr) == len(constraints[0][0]):
			index_pointers.append(ptr)
			# print(ptr)
			index_ptr = []
			for i in range(len(ptr)):
				if ptr[i] == 1:
					index_ptr.append(i)

			print(index_ptr)
			packages.append(append_package(constraints, index_ptr))
	# print(packages)
	return packages

# def point_if_feasible(point, constraints):
# 	for strict in constraints:
# 		if (np.dot(strict[0], point) < strict[1])


if __name__ == '__main__':
	# print(get_packages([((1,1),0), ((-2,1),1), ((1, 3), 8)]))
	# print(ptr_cnt([3,4,5],6, 1, False))
	print(function([((-1,-1,-1,0,0,0), -15),
((0,0,0,-1,-1,-1), -30),
((1.2,1.3,1.1,0,0,0),30),
((0,0,0,1.2,1.3,1.1),30),
((-1,0,0,0,0,0), 0),
((0,-1,0,0,0,0), 0),
((0,0,-1,0,0,0), 0),
((0,0,0,-1,0,0), 0),
((0,0,0,0,-1,0), 0),
((0,0,0,0,0,-1), 0)]
))
	# print(find_one_intersection([((0,1),10), ((-1, 0),0)]))
	# print(get_packages([((1, 0), 10), ((0, 1), 10), ((-1, 0), 0), ((0, -1), 0)]))