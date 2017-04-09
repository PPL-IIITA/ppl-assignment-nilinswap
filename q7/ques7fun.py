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
def findout1(boyiz, newcouplelist):
	if boyiz.name in [item.bo.name for item in newcouplelist]:
		ind=[item.bo.name for item in newcouplelist].index(boyiz.name)
		return newcouplelist[ind].gir
	else:
		return None
def findout2(boyiz,dic):
	if boyiz.name in dic.keys():
		return dic[boyiz.name]
	else:
		return None
def hashfun(boyiz,newcouplelist):
	if boyiz.name in [item.bo.name for item in newcouplelist]:
		ind=[item.bo.name for item in newcouplelist].index(boyiz.name)
		return ind
	else:
		return -1
def findout3(boyiz,newcouplelist):
	ind= hashfun(boyiz,newcouplelist)
	if ind>=0:	
		return newcouplelist[ind].gir
	else :
		return None
		
