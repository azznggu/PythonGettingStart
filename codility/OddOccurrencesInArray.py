'''
array A consisting of N integers fulfilling the above conditions, 
returns the value of the unpaired element.

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''

def solution(list):
	r = 0
	for i in range(len(list)):
		r ^= list[i]
	return r



A = [4,3,5,5,4]
print(solution(A))