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
	i=0
	if not i:
		couplelist=compartor.compartor1(templisb,lisg)
	else:
		couplelist=compartor.compartor(templisb,lisg)
	print("question 5:\n")
	
	newcouplelist=makecouple.makecouple(couplelist)
	
	print("there are total %d couples. \n"%len(couplelist))
	k=random.randrange(1,len(newcouplelist))
	ques2fun.printmaxhpns(newcouplelist,k)
	ques2fun.printmaxcpt(newcouplelist,k)
	print("here are gifts\n")
	ques2fun.printallgifts()
main()
