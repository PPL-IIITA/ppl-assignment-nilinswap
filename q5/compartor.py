def boshortlister(gir,lisb):#shortlists boys on basis of their budget as per girl and boy's minimum requirement
	lis=[]
	for bo in lisb:
			if gir.mntcst<=bo.budget and gir.hotn>=bo.minhotn:
				lis.append(bo)
	return lis
def girshortlister(bo,lisg):
	lis=[]
	for gir in lisg:
			if gir.mntcst<=bo.budget :
				lis.append(gir)
	return lis
def compartor1(lisb,lisg):
	rtrnlis=[]#this is the list of tuples that has to be returned
	templisb=lisb[:]
	templisg=lisg[:]
	templisg.sort(key=lambda x:x.hotn,reverse=True)
	templisb.sort(key=lambda x:x.budget,reverse=True)
	cou=0
	while  templisg and templisb:
		if cou%2==0:
			gir=templisg[0]
			templisg.remove(gir)
			shrtlisb=boshortlister(gir,templisb)
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
				templisb.remove(shrtlisb[maxin])#this removes the selected boy from lisb but as lists are mutable we have to make a copy of lisb before calling this and lisg doesn't change
			
			elif gir.choice=='r':
				maxr=-1
				maxin=0
				for ind in range(len(shrtlisb)):
					if shrtlisb[ind].budget>maxr:
						maxr=shrtlisb[ind].budget
						maxin=ind
				rtrnlis.append((shrtlisb[maxin],gir))
				templisb.remove(shrtlisb[maxin])
		
			else:
				maxi=-1
				maxin=0
				for ind in range(len(shrtlisb)):
					if shrtlisb[ind].clvrn>maxi:
						maxi=shrtlisb[ind].clvrn
						maxin=ind
				rtrnlis.append((shrtlisb[maxin],gir))
				templisb.remove(shrtlisb[maxin])
		else:
			bo=templisb[0]
			templisb.remove(bo)
			shrtlisg=girshortlister(bo,templisg)
			if not shrtlisg:#that is if there is no boy meeting girl's expectation girl, move on to next girl.
				continue
			maxa=-1
			maxin=0
			for ind in range(len(shrtlisg)):
				if shrtlisg[ind].hotn>maxa:
					maxa=shrtlisg[ind].hotn
					maxin=ind
			rtrnlis.append((bo,shrtlisg[maxin]))#this appends to rtrnlis couples
			templisg.remove(shrtlisg[maxin])#this removes the selected boy from lisb but as lists are mutable we have to make a copy of lisb before calling this and lisg doesn't change
		cou+=1
	return rtrnlis	
def compartor(lisb,lisg):
	rtrnlis=[]#this is the list of tuples that has to be returned
	for gir in lisg:
		shrtlisb=boshortlister(gir,lisb)
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
