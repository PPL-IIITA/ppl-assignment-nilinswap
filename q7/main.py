import inputter
import random
import boy
import girl
import compartor
import couple
import inputhelper
import makecouple
import ques7fun
def main():
	nb=random.randrange(5,10)
	ng=2*nb
	inputhelper.girlrandomgenerator(ng)
	inputhelper.boyrandomgenerator(nb)
	lisg=inputter.girlinputreaderandmaker()
	lisb=inputter.boyinputreaderandmaker()	
	templisb=lisb[:]# creating a duplicate list, see templisb=lisb will not work as they both reference the same thing
	couplelist=compartor.compartor(templisb,lisg)
	print("question 7:\n")
	
	newcouplelist=makecouple.makecouple(couplelist)
	boyiz=random.choice(lisb)
	i=0#it's programmers choice how he wants to find out
	
	print("for boy %s"%boyiz.name)
	if not i:
		girl=ques7fun.findout1(boyiz,newcouplelist);
		if girl:
			print(girl.name)
		else:
			print("not found, i.e. he is single\n")
	elif i==1:
		dic={item.bo.name:item.gir.name for item in newcouplelist}
		girl=ques7fun.findout2(boyiz,dic);
		if girl:
			print(girl)
		else:
			print("not found, i.e. he is single\n")
		
	else:
		girl=ques7fun.findout3(boyiz,newcouplelist)
		if girl:
			print(girl.name)
		else:
			print("not found, i.e. he is single\n")
main()
