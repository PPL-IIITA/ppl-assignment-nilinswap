import math
class commgirl:
	def __init__(self,name,hotn,smrtn,mntcst,choice,bo,typ):
		self.name=name
		self.hotn=hotn#girl's hotness: a no. from 0-9
		self.smrtn=smrtn#girl's smartness: a no. from 0-9
		self.mntcst=mntcst#girl's maintainence cost: a no. from 0-999
		self.choice=choice#girl's choce: a no. from a set of {'a','r','i'} , 'a' for most attractive, 'r' for most richest and 'i' for most intelligent
		self.bo=bo
		self.typ=typ#type: a letter from set {'c','n','d'} c for choosy, n for normal and d for desperate
	def happinesscalculator(self):
		if self.typ=='c':
			self.hpns=math.log(self.bo.mnyspt-self.mntcst)+(self.bo.totvalue+self.bo.lgiftv)#  a girl's happiness as an attribute
		elif self.typ=='n':
			self.hpns=(self.bo.mnyspt-self.mntcst)/100+self.bo.totvalue
		else :
			self.hpns=math.exp(self.bo.mnyspt-self.mntcst)
			
