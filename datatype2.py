#string
s = "i am a string."
print(type(s))		#return string 

#boolean
yes = True			#boolean true
print(type(yes))	

no = False			#boolean false
print(type(no))

#list --ordered amd changeable

alpha_list = ["a","b","c"]	#list initialization
print(type(alpha_list))		#will say tuple
print(type(alpha_list[0]))	#will say string 
alpha_list.append("d")		#will add "d" to the list end
print(alpha_list)			#will print list

#Tuple -- ordered and unchangeable
alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))		#will say tuple

try: 			#attempt the following line
	alpha_tuple[2] = "d"	#wont work will raise type error
except TypeError: 
	print("we can't add elements to tuples")
print(alpha_tuple)		#will print tuple

