#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class"		:	"Astro 119"
	"prof"		: 	"Brant"
	"awesomeness" : 10

}
print(type(example_dict))	#will say dict

#get a value via key
example_dict["awesomeness"] += 1	#increase awesomeness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.key():
	print(x,example_dict[x])