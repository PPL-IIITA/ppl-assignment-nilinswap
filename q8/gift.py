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
	
	def threeofeach(self):
		lis=self.sortasperprice()
		templis=[]
		flag1=flag2=flag3=0
		for item in lis:
			if type(item).__name__=='egift' and flag1==0:
				templis.append(item)
				lis.remove(item)
				flag1=1
			if type(item).__name__=='lgift' and flag2==0:
					templis.append(item)
					lis.remove(item)
					flag2=1
			if type(item).__name__=='ugift' and flag3==0:
				templis.append(item)
				lis.remove(item)
				flag3=1
			if flag1 and flag2 and flag3:
				return templis
