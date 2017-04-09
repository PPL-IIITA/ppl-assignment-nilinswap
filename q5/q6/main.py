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
	print("ques 6\n")
	newcouplelist=makecouple.makecouple(couplelist)
	k=random.randrange(1,len(newcouplelist))
	t=random.randrange(2,9)
	i=1
	for item in newcouplelist:
			print("boy: %s and girl: %s"%(item.bo.name,item.gir.name))
	
	while i<=t:
		newcouplelist=ques4fun.breakup(lisb,newcouplelist,i)
		print("after %d days"%i)
		if not newcouplelist:
			print("anything")
		for item in newcouplelist:
			print("boy: %s and girl: %s"%(item.bo.name,item.gir.name))
		i+=1 
	
	
main()
