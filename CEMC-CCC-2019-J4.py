array = [1,2,3,4]
flip = str(input(""))
for i in flip:
	if i == "H":
		array = [array[2] , array[3] , array[0] , array[1]]
	if i == "V":
		array= [array[1] , array[0] , array[3] , array[2]]
print("{} {}".format(array[0] , array[1]))
print("{} {}".format(array[2] , array[3]))
