import random

dice=['1','2','3','4','5','6']
u_inp=input("enter your number ")


if ( u_inp<='6' and u_inp>='0'):
	if(u_inp == random.choice(dice)):
		print("Winner")
	else:
		print("Better luck next time")
	
else:
	print("check your number",u_inp)


