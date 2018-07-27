#Blood_Donation

class Person(object):
	def __init__(self,name=None,phone=None,bloodgroup=None,age=None,district=None,lastdate=None,delta=None):
		self.name=name
		self.phone=phone
		self.bloodgroup=bloodgroup
		self.age=age
		self.district=district
		self.lastdate=lastdate
		self.delta=delta
personList = []
import datetime
def insert():
	"""For inserting values."""
	global a
        global count
	gr=["A-","A+","B-","B+","O-","O+","AB-","AB+"]
	dic=["kasaragod","kannur","kozhikode","wayanad","malappuram","palakkad","thrissur","ernakulam","kottayam","idukki","alappuzha","pathanamthitta","kollam","thiruvananthapuram"]
	name=raw_input("name of donor\n")
	if name=='':
		print "\tname field empty"
		name=raw_input("name of donor\n")
	if name.isdigit()==True:
		print "\tname field not contain numbers"
		name=raw_input("name of donor\n")
	
	phone=raw_input("enter your phone number\n")
	if phone=='':
		print "\t phone field id empty\n"
		phone=raw_input("enter your phone number\n")
	if phone.isdigit()==False:
		print "\t phone field not contain string\n"
	if len(phone)!=10:
		print "print a 10 digit phone number"
		phone=raw_input("enter your phone number\n")
	print "select your blood type A-,A+,B+,B-,O-,O+,AB-,AB+"
	type1=raw_input("enter your blood group\n")
	if type1=='':
		print "blood type field is empty"
	if type1.isdigit()==True:
		print "\t blood type field not contain number"
		type1=raw_input("enter your blood group\n")
	
	c=0
	for i in range(8):
		if type1==gr[i]:
			bloodgroup=type1
		else:
			c=c+1
		if c==8:
			print "wrong blood group",type1
			type1=raw_input("enter your blood group\n")
			bloodgroup=type1
	def d():
		"""Checking age."""
		while True:
			age=raw_input("enter your age\n")
			if str(age).isdigit()==False:
				print "please enter your age correct " 
				age=input("enter your age\n")
			age=int(age)
			if age<18 or age>70:
				print "you are not eligible to donate blood"
			age=int(age)
			if age>18 and age<70:
				break
		return age
	age=d()
	print "enter your district choices 1 to 14"
	for i in range(14):
		print "",i+1,"",dic[i]
	def dict():
		"""District validation."""
		while True:
			district1=raw_input()
			if str(district1)=='':
				print "\tdistrict feild empty"
				district1=input("enter your district choice\n")
			district1=int(district1)
			if district1>=1 and district1<=14:
				for i in range(14):
					if dic[i]==dic[district1-1]:
						return dic[district1-1]
						break
	
	district=dict()				
	print district
	def vali(lastdate):
		"""Date validation."""
		try:
			if lastdate!=datetime.datetime.strptime(lastdate, '%Y-%m-%d'):
				print
			return True
		except ValueError:
			return False		
	lastdate=raw_input("last donated YYYY-MM-DD format\n")
	if lastdate=='':
		print "date is blank"
		lastdate=raw_input("last donated YYYY-MM-DD format\n")
	u=vali(lastdate)
	while True:
		u=vali(lastdate)
		if u==False:
			lastdate=raw_input("please re enter donated date in YYYY-MM-DD format\n")
			vali(lastdate)
		elif u==True:
			break
	today = datetime.date.today()
	lastdate = datetime.datetime.strptime(lastdate, "%Y-%m-%d").date()
	delta =  (today - lastdate).days
        delta=int(delta)
	personList.append(Person(name,phone,bloodgroup,age,district,lastdate,delta))
	return 
def printb():
	global a
	print "NAME\t PHONE\t\tGROUP\t AGE\tLOCATION\tDATE  \t   DURATION IN DAYS"
	for j in range(a):
		print personList[j].name,"\t",personList[j].phone,"\t",personList[j].bloodgroup,"\t",personList[j].age,"\t",personList[j].district,"\t",personList[j].lastdate," ",personList[j].delta	
def p(j):
	print personList[j].name,"\t",personList[j].phone,"\t",personList[j].bloodgroup,"\t",personList[j].age,"\t",personList[j].district," \t",personList[j].lastdate," ",personList[j].delta
def o(i):
	print personList[i].name,"\t",personList[i].phone,"\t",personList[i].bloodgroup,"\t",personList[i].age,"\t",personList[i].district," \t",personList[i].lastdate," ",personList[i].delta

def sort(k,l,b):
	"""For finding match."""
	global count
	global a
	q=0
	x=["O-","O+","A-","A+","B-","B+","AB-","AB+"]
	blood=[]
	del blood[:]
	del x[:]
	if q==0:
		for i in range(a):
			blood.append(personList[i].bloodgroup)
			q=q+1
	
	print "\n\n........SORTED LIST..............",k
	print "NAME\t PHONE\t\tGROUP\t AGE\tLOCATION\tDATE  \t   DURATION IN DAYS"
	def h():
		print "\n\n........NEAREST PLACE..............",k
		print "NAME\t PHONE\t\tGROUP\t AGE\tLOCATION\tDATE  \t   DURATION IN DAYS"
	if k==1:
		y=0
		for j in range(a):
			if personList[j].bloodgroup=="O-" and personList[j].delta >60 and personList[j].district==l :
				p(j)
				y=y+1
		if y==0:	
			print "\nno list found\n"
				
		j=0
		h()
		for i in range(a):
			if (personList[i].bloodgroup=="O-" and personList[i].delta >60 and personList[i].district!=l) and personList[i].district==b[0]:
				j=j+1
				o(i)
			if (personList[i].bloodgroup=="O-" and personList[i].delta >60 and personList[i].district!=l) and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"

	elif k==2:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="O+") and (personList[j].delta >60 and personList[j].district==l):		
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"
		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+")and personList[i].delta >60 and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)	
			if((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+")and personList[i].delta >60 and personList[i].district!=l)and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"
	elif k==3:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="A-" or personList[j].bloodgroup=="O-") and (personList[j].delta >60 and personList[j].district==l):
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"

		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="O-") and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)
			if ((personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="O-") and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"

	elif k==4:
		y=0
		for j in range(a):
			if ((personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="O+" or personList[j].bloodgroup=="A-" or personList[j].bloodgroup=="A+")and personList[j].delta >60 )and personList[j].district==l:
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"
		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="A+")and personList[i].delta >60 and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="A+")and personList[i].delta >60 and personList[i].district!=l)and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"
				
	elif k==5:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="B-")and personList[j].delta >60 and personList[j].district==l:
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"
		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="O-") and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)
			if ((personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="O-") and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"

	elif k==6:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="O+" or personList[j].bloodgroup=="B-" or personList[j].bloodgroup=="B+")and personList[j].delta >60 and personList[j].district==l:
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"

		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="B+")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="B+")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(j)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"
		
	elif k==7:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="A-" or personList[j].bloodgroup=="B-" or personList[j].bloodgroup=="AB-")and personList[j].delta >60 and personList[j].district==l:
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"	
		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="AB-")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)  
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="AB-")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[1]: 
				j=j+1
				o(j)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"
	elif k==8:
		y=0
		for j in range(a):
			if (personList[j].bloodgroup=="O-" or personList[j].bloodgroup=="O+" or personList[j].bloodgroup=="A-" or personList[j].bloodgroup=="A+" or personList[j].bloodgroup=="B-" or personList[j].bloodgroup=="B+" or personList[j].bloodgroup=="AB-" or personList[j].bloodgroup=="AB+")and personList[j].delta >60 and personList[j].district==l:
				y=y+1
				p(j)
		if y==0:
			print "\nno list found\n"
		j=0
		h()
		for i in range(a):
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="A+" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="B+" or personList[i].bloodgroup=="AB-" or personList[i].bloodgroup=="AB+")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[0]:
				j=j+1
				o(i)
			if ((personList[i].bloodgroup=="O-" or personList[i].bloodgroup=="O+" or personList[i].bloodgroup=="A-" or personList[i].bloodgroup=="A+" or personList[i].bloodgroup=="B-" or personList[i].bloodgroup=="B+" or personList[i].bloodgroup=="AB-" or personList[i].bloodgroup=="AB+")and personList[i].delta >60  and personList[i].district!=l)and personList[i].district==b[1]:
				j=j+1
				o(i)
		if j==0:
			print "\n sorry there is no blood available in nearest place\n"

	else:
		print "wrong choice"

def s():
	"""For passing values for district and neighbours"""
	dic=["kasaragod","kannur","kozhikode","wayanad","malappuram","palakkad","thrissur","ernakulam","kottayam","idukki","alappuzha","pathanamthitta","kollam","thiruvananthapuram"]
	g=input("1 to search blood group \n2 to print details \n3 to exit\n ")
	if g==1:
		print "please select your blood group"
		k=input("1 for o-\n2 for 0+\n3 for A-\n4 for A+\n5 for B-\n6 for B+\n7 for AB-\n8 for AB+\n ")
		print "enter your district choices 1 to 14"		
		for i in range(14):
			print "",i+1,"",dic[i]	
		def dict():
			while True:
				district1=raw_input()
				if str(district1)=='':
					print "\tdistrict feild empty"
					district1=input("enter your district choice\n")
				district1=int(district1)
				if district1>=1 and district1<=14:
					for i in range(14):
						if dic[i]==dic[district1-1]:
							if district1==1:
								r1=dic[1],dic[2]
							elif district1==14:
								r1=dic[12],dic[11]
							else:
								r1=dic[district1-2],dic[district1]
							return dic[district1-1],r1	
							break	
		l,b=dict()
		print "you selected ",l
		print "nearest place",b
		sort(k,l,b)
		s()
	elif g==2:
		printb()
		s()
	elif g==3:
		print (exit())
	else:
		print "wrong key"
		s()

a=input("enter how many records you want")
count=0
for i in range(0,a):
	print "enter details of Donor ",i+1	
	insert()
	count=count+1

s()
	



