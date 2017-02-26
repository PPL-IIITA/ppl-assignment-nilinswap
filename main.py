import inputter
import random
import boy
import girl
import compartor
import couple
import inputhelper
import makecouple
import ques2fun
def main():
	nb=random.randrange(5,10)
	ng=2*nb
	inputhelper.girlrandomgenerator(ng)
	inputhelper.boyrandomgenerator(nb)
	lisg=inputter.girlinputreaderandmaker()
	lisb=inputter.boyinputreaderandmaker()	
	templisb=lisb[:]# creating a duplicate list, see templisb=lisb will not work as they both reference the same thing
	couplelist=compartor.compartor(templisb,lisg)
	print("question 1: formed couples are\n")
	for item in couplelist:
		print("boy: '%s' with girl: '%s'\n"%(item[0].name,item[1].name))
	newcouplelist=makecouple.makecouple(couplelist)
	print("\n\nquestion 2:\n")
	print("there are total %d couples. input k \n"%len(couplelist))
	k=int(input())
	ques2fun.printmaxhpns(newcouplelist,k)
	ques2fun.printmaxcpt(newcouplelist,k)
	print("there are too many gifts.Are you sure you want to see all of them? type 1 if yes else 0")
	opt=input()
	if opt=='1':
		ques2fun.printallgifts()
main()
