import numpy as np #np is very nb

def main():
	i = 0		#integer
	n = 10		#integer
	x =119.0	#floating point

	#declare arrays

	y = np.zeros(n,dtype=float) #declare 10 zeros as floats using np

	# we can use for loops to iterate with a variable

	for i in range(n): 	#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1. 	#set y = 2i+1 as floats

	#iterate through a variable
	for y_element in y:
		print(y_element)
#execute the main function
if __name__ == "__main__":
	main()