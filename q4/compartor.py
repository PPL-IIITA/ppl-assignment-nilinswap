def shortlister(gir,lisb):#shortlists boys on basis of their budget as per girl and boy's minimum requirement
	lis=[]
	for bo in lisb:
			if gir.mntcst<=bo.budget and gir.hotn>=bo.minhotn:
				lis.append(bo)
	return lis
def compartor(lisb,lisg):
	rtrnlis=[]#this is the list of tuples that has to be returned
	for gir in lisg:
		shrtlisb=shortlister(gir,lisb)
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
