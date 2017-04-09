import boy
import girl
import random
import gift
"""def boyrandomgenerator(nb):
	alrang='abcdefghijklmnopqrstuvwxyz'
	lisb=[]
	for i in range(nb):
		name=''.join([random.choice(alrang) for i in range(10)])
		clvrn=random.randint(0,10)
		budget=random.randint(0,1000)
		sxn=random.randint(0,10)
		minhotn=random.randint(0,10)
		newb=boy.boy(name,clvrn,sxn,minhotn,budget)
		lisb.append(newb)
	return lisb"""

def girlrandomgenerator(ng):#randomly generates girls' data and write it into input file to be read by inputter function
	alrang='abcdefghijklmnopqrstuvwxyz'
	lisg=[]
	filob=open("input.txt","w")
	for i in range(ng):
		name=''.join([random.choice(alrang) for i in range(10)])
		smrtn=random.randint(0,10)
		mntcst=random.randint(0,1000)
		hotn=random.randint(0,10)
		choice=random.choice(['a','r','i'])
		filob.write("%s %d %d %d %s\n"%(name,hotn,smrtn,mntcst,choice))
	filob.write("---\nabove was girls' data\n***\n")
	filob.close()
	
def boyrandomgenerator(nb):
	alrang='abcdefghijklmnopqrstuvwxyz'
	lisg=[]
	filob=open("input.txt","a")#its very important to see that the boy data comes after girl's in input therefore mode is 'a'
	lisb=[]
	for i in range(nb):
		name=''.join([random.choice(alrang) for i in range(10)])
		clvrn=random.randint(0,10)
		budget=random.randint(0,1000)
		sxn=random.randint(0,10)
		minhotn=random.randint(0,10)
		filob.write("%s %d %d %d %s\n"%(name,clvrn,sxn,minhotn,budget))
		
	filob.write("---\nabove was boys' data\n***\n")
"""def girlrandomgenerator(ng):
	alrang='abcdefghijklmnopqrstuvwxyz'
	lisg=[]
	for i in range(ng):
		name=''.join([random.choice(alrang) for i in range(10)])
		smrtn=random.randint(0,10)
		mntcst=random.randint(0,1000)
		hotn=random.randint(0,10)
		choice=random.choice(['a','r','i'])
		newg=girl.girl(name,hotn,smrtn,mntcst,choice)
		lisg.append(newg)
	return lisg"""
def basketrandomgenerator():
	n=random.randint(44,100)
	lis=[]
	for i in range(n):
		val=random.randint(0,9)
		price=random.randrange(30,120,8)
		utlcls=random.choice(['dress','makeup','footwear'])
		utlval=random.randint(0,9)
		lux=random.randint(0,9)
		diff=random.randint(0,9)
		gif=random.choice([gift.egift(val,price),gift.lgift(val,price,lux,diff),gift.ugift(val,price,utlcls,utlval)])
		lis.append(gif)
	baske=gift.basket(lis)
	return baske
		
