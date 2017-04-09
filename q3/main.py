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
	print("question 3:\n")
	
	newcouplelist=makecouple.makecouple(couplelist)
	print("\n\nquestion 2 using inheritance:\n")
	print("there are total %d couples. \n"%len(couplelist))
	k=random.randrange(1,len(newcouplelist)-1)
	ques2fun.printmaxhpns(newcouplelist,k)
	ques2fun.printmaxcpt(newcouplelist,k)
	print("here are gifts\n")
	ques2fun.printallgifts()
main()
