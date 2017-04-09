import inputter
import random
import boy
import girl
import compartor
import couple
import inputhelper
import makecouple
import ques4fun
def main():
	nb=random.randrange(5,10)
	ng=2*nb
	inputhelper.girlrandomgenerator(ng)
	inputhelper.boyrandomgenerator(nb)
	lisg=inputter.girlinputreaderandmaker()
	lisb=inputter.boyinputreaderandmaker()	
	templisb=lisb[:]# creating a duplicate list, see templisb=lisb will not work as they both reference the same thing
	couplelist=compartor.compartor(templisb,lisg)
	print("ques 4\n")
	newcouplelist=makecouple.makecouple(couplelist)
	k=random.randrange(1,len(newcouplelist))
	
	removedlist=ques4fun.removeminhpns(newcouplelist,k)
	
	 
	
	
	couplelist=ques4fun.q4compartor(lisb,removedlist)
	newcouplelist=makecouple.makecouple(couplelist)
	print("finally")
	for item in newcouplelist:
		print("girl : %s and boy: %s\n"%(item.gir.name,item.bo.name)) 
	
	
main()
