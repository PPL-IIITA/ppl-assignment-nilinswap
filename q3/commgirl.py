import math
import girl
class commgirl(girl.girl):
	def __init__(self,name,hotn,smrtn,mntcst,choice,bo,typ):
		girl.girl.__init__(self,name,hotn,smrtn,mntcst,choice)
		self.bo=bo
		self.typ=typ#type: a letter from set {'c','n','d'} c for choosy, n for normal and d for desperate
		self.hpns=0
class choosy(commgirl):
	def __init__(self,name,hotn,smrtn,mntcst,choice,bo,typ):
		commgirl.__init__(self,name,hotn,smrtn,mntcst,choice,bo,typ)
	
	def happinesscalculator(self):
			self.hpns=math.log(self.bo.mnyspt-self.mntcst)+(self.bo.totvalue+self.bo.lgiftv)#  a girl's happiness as an attribute
class normal(commgirl):
	def __init__(self,name,hotn,smrtn,mntcst,choice,bo,typ):
		commgirl.__init__(self,name,hotn,smrtn,mntcst,choice,bo,typ)
	
	def happinesscalculator(self):
			
			self.hpns=(self.bo.mnyspt-self.mntcst)/100+self.bo.totvalue
		
class desperate(commgirl):
	def __init__(self,name,hotn,smrtn,mntcst,choice,bo,typ):
		commgirl.__init__(self,name,hotn,smrtn,mntcst,choice,bo,typ)
	
	def happinesscalculator(self):
			self.hpns=math.exp(self.bo.mnyspt-self.mntcst)

