import numpy as np #numpy lib

#integers

i = 10 	#integer
print(type(i))	#print out the data type of i

a_i = np.zeros(i,dtype=int) #declare an array of ints
print(type(a_i)) 	#will return ndarray
print(type(a_i[0]))	#will return int64

#floats
x = 119.0	#floating point number
print(type(x)) #print out the data type of x

y = 1.19e2	#scientific notation
print(type(y)) #print the data type of y

z = np.zeros(i,dtype=float)	#decalare array of floats
print(type(z))				# will retuen nd array 
print(type(z[0]))			#will return float64
