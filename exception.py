#python exceptions let you deal with
#unexpected results

try: 
	print(a) 	#this will not work, a is not defined
except:
	print("a is not defined")

#there are specific errors to help with cases
try: 
	print(a)	#this will throw exception since a is not defined
except NameError: 
	print("a is still not defined!")
except:
	print("something else went wrong")

#the followong will break the program 
#since a is still not defined
print(a)