#define a function
def flow_control(K):

	#define a string based on the value of k
	if(k==0):
		s = "variable k = %d equals 0." % k
	else(k==1):
		s = "variable k = %d equals 1." % k
	else: 
		s = "variable k = %d does not equal 0 or 1." % k

		#print the variable
		print(s)

	#define a main function 
	def main(): 

		#decalre an integer
		i = 0

		#try flow_control for 0, 1,2
		flow_control(i)
		i = 1 
		flow_control(i)
		i = 2
		flow_control(i)

		#run the program
		if __name__ == "__main__":
			main()