li = []
new = []
total = 0
final = []
n = int(input(""))
count = -1
for i in range(n):
	a = str(input(""))
	for j in a:
		count += 1
		if count+1 <= len(a)-1:
			if a[count+1] == a[count]:
				li.append(count)
			else:
				value = ("{} {}".format(len(li)+1 , a[count]))
				total += len(li)+1
				new.append(value)
				li = []
	new.append("{} {}".format(len(a)-total , a[len(a)-1]))
	def conversion(new):
		convert = ""
		for item in new:
			convert += item
			convert += " "
		return convert
	final.append(conversion(new))
	count = -1
	total = 0
	new = []
	li = []
for k in final:
	print(k)
