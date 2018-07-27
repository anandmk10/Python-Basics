a=[1,2,[1,2,[5,7]],[3,4]]
b=[]
for i in a:
	try:
		for j in i:
			try:
				for k in j:
					b.append(k)
			except:
				b.append(j)
	except:
		b.append(i)
print(b)
				


