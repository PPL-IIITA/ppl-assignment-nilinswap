import commboy
import commgirl
import random
import inputhelper
import couple
def makecouple(couplelist):
	newcouplelist=[]
	p=0
	coun=1
	filob=open("log.txt","w")#this mode so that log.txt is overwritten
	filob.write("commited couples\n\n")
	for item in couplelist:
		p=random.choice(['c','n','d'])#chooses a random kind of girl
		item1=commgirl.commgirl(item[1].name,item[1].hotn,item[1].smrtn,item[1].mntcst,item[1].choice,item[0],p)
		item0=commboy.commboy(item[0].name,item[0].clvrn,item[0].sxn,item[0].minhotn,item[0].budget,item1,p)
		
		item1=commgirl.commgirl(item[1].name,item[1].hotn,item[1].smrtn,item[1].mntcst,item[1].choice,item0,p)
		baske=inputhelper.basketrandomgenerator()
		item0.giftallocator(baske)
		item1.happinesscalculator()
		item0.happinesscalculator()
		onecouple=couple.couple(item0,item1)
		newcouplelist.append(onecouple)
		strin="%d. guy's name : %s      girl's name: %s\ngifts are \n"%(coun,item0.name,item1.name)
		filob.write(strin)
		cou=1
		for gif in item0.giftbag:
			strin="%d value: %d,  price: %d, type: %s\n"%(cou,gif.value,gif.price,type(gif).__name__)
			filob.write(strin)
			cou+=1
		filob.write("\n")
		coun+=1
	filob.close() 
		
	return newcouplelist
