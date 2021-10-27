a = []
b = []
count = 0
for i in range(6):
	count += 1
	point = int(input(""))
	if count <= 3:
		a.append(point)
	else:
		b.append(point)
if a[0]*3+a[1]*2+a[2] > b[0]*3+b[1]*2+b[2]:
	print("A")
elif a[0]*3+a[1]*2+a[2] < b[0]*3+b[1]*2+b[2]:
	print("B")
else:
	print("T")
