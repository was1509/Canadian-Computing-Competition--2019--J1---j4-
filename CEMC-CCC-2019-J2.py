mylist = []
final = []
count = 0
l = int(input(""))
for i in range(l):
	value = str(input(""))
	for j in value.split():
		if j != " ":
			mylist.append(j)
	final.append(mylist[1]*int(mylist[0]))
	mylist = []
for k in final:
	print(k)
