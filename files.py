fp = open("s1.txt","w")
fp.write("success file")
fp.write("success file55")
fp.close()

fp = open("s1.txt","r+")
print("File contents:",fp.readline())

fp.append("appended")

fp.seek(0,0)
print("current position",fp.tell())
fp.seek(7)
print("current position after",fp.tell())

fp.close()
