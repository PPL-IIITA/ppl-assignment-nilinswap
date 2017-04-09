def printmaxhpns(lis,k):
	templis=lis[:]
	templis.sort(key=lambda x:x.hpns,reverse=True)
	print(" %d happiest couples are :\n"%k) 
	for coup in templis[:k]:
		print("boy: %s and girl: %s with happiness pts: %d\n"%(coup.bo.name,coup.gir.name,coup.hpns))
def printmaxcpt(lis,k):
	templis=lis[:]
	templis.sort(key=lambda x:x.cmpblty,reverse=True)
	print(" %d most compatiable couples are :\n"%k) 
	for coup in templis[:k]:
		print("boy: %s and girl: %s with compatablity pts: %d\n"%(coup.bo.name,coup.gir.name,coup.cmpblty))
def printallgifts():
	filob=open("log.txt",'r')
	st=filob.read()
	print("gifts as per couple are:\n")
	print(st)
	filob.close()
