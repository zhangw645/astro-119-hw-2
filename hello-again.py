#define the main() function
def main():

	i = 0		#declare interger i
	x = 119.0	#declare float x

	for i in range(120): #loop i from 0 to 119, inclusive
		if((i%2)==0): 	#if i is even
			x += 3. 	#add 3 to x
		else:			#if not true
			x -= 5.		#substract 5 from x

			s = "%3.2e" % x 	#make a string containing x with sci. notation of 2 decimals

		print(s)	#print s to the screen

		if __name__=="__main__": #if the main() function exists,run it
			main()