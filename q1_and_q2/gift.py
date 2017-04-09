class egift:
	def __init__(self,value,price):
		self.value=value
		self.price=price
class lgift:
	def __init__(self,value,price,lux,diff):
		self.lux=lux
		self.value=value
		self.price=price
		self.diff=diff
class ugift:
	def __init__(self,value,price,utlcls,utlval):
		self.value=value
		self.price =price
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
	
	
	
