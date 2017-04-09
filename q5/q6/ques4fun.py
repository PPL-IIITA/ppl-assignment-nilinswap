import makecouple
def removeminhpns(lis,i):
	templis=lis[:]
	templis.sort(key=lambda x:x.hpns)
	ind=0
	lisi=[]
	while ind<len(templis) and templis[ind].hpns<i:
		coup=templis[ind]
		lisi.append(coup)
		lis.remove(coup)
		ind+=1
	return lisi
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
def shortlister(gir,lisb):#shortlists boys on basis of their budget as per girl and boy's minimum requirement
	lis=[]
	for bo in lisb:
			if gir.mntcst<=bo.budget and gir.hotn>=bo.minhotn:
				lis.append(bo)
	return lis
def q4compartor(lisb,removedlist):
	rtrnlis=[]#this is the list of tuples that has to be returned
	for item in removedlist:
		gir=item.gir
		shrtlisb=shortlister(item.gir,lisb)
		if not shrtlisb:#that is if there is no boy meeting girl's expectation girl, move on to next girl.
			continue
	
		if gir.choice=='a':
			maxa=-1
			maxin=0
			for ind in range(len(shrtlisb)):
				if shrtlisb[ind].sxn>maxa:
					maxa=shrtlisb[ind].sxn
					maxin=ind
			rtrnlis.append((shrtlisb[maxin],gir))#this appends to rtrnlis couples
			lisb.remove(shrtlisb[maxin])#this removes the selected boy from lisb but as lists are mutable we have to make a copy of lisb before calling this and lisg doesn't change
			
		elif gir.choice=='r':
			maxr=-1
			maxin=0
			for ind in range(len(shrtlisb)):
				if shrtlisb[ind].budget>maxr:
					maxr=shrtlisb[ind].budget
					maxin=ind
			rtrnlis.append((shrtlisb[maxin],gir))
			lisb.remove(shrtlisb[maxin])
		
		else:
			maxi=-1
			maxin=0
			for ind in range(len(shrtlisb)):
				if shrtlisb[ind].clvrn>maxi:
					maxi=shrtlisb[ind].clvrn
					maxin=ind
			rtrnlis.append((shrtlisb[maxin],gir))
			lisb.remove(shrtlisb[maxin])
	return rtrnlis
def breakup(lisb,newcouplelist,i):
	removedlist=removeminhpns(newcouplelist,i)
	templisb=lisb[:]
	couplelist=q4compartor(templisb,removedlist)
	if couplelist:
		print("anything else")
	couplelist=makecouple.makecouple(couplelist)
	return newcouplelist+couplelist
	
