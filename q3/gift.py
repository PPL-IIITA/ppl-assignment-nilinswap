class gift:
	def __init__(self,value,price):
		self.value=value
		self.price=price

class egift(gift):
	def __init__(self,value,price):
		gift.__init__(self,value,price)
class lgift(gift):
	def __init__(self,value,price,lux,diff):
		gift.__init__(self,value,price)
		self.lux=lux
		self.diff=diff
class ugift(gift):
	def __init__(self,value,price,utlcls,utlval):
		gift.__init__(self,value,price)
		self.utlcls=utlcls
		self.utlval=utlval
class basket:
	def __init__(self,lis):
		self.baslis=lis
	def sortasperprice(self):
		templis=self.baslis[:]
		templis.sort(key=lambda x:x.price)
		return templis
	def reversesortasperprice(self):
		templis=self.baslis[:]
		templis.sort(key=lambda x:x.price,reverse=True)
		return templis
	
	
	
