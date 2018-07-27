a=[0,[1,2],[3,4]]
b=[]
for i in a:
	try:
		for j in i:
			b.append(j)
	except:
		b.append(i)
print(b)
