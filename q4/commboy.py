import gift
import boy
import girl
class commboy(boy.boy):#after the boy gets committed
	def __init__(self,name,clvrn,sxn,minhotn,budget,gir):
		boy.boy.__init__(self,name,clvrn,sxn,minhotn,budget)
		self.gir=gir#the girl he is dating
		
		
		#here this decides which gift the boy chooses
	
		
class miser(commboy):
	def __init__(self,name,clvrn,sxn,minhotn,budget,gir):
		commboy.__init__(self,name,clvrn,sxn,minhotn,budget,gir)
	
	def giftallocator(self,baske):#here baske is basket type
		self.giftbag=[]#another attribute;committed boy's giftbag
		self.lgiftv=0	#another attribute;this sees total value for luxary gift as liked by choosy girls
		totval=0
		self.mnyspt=0
		lis=baske.sortasperprice()			#sort basket as per low to high price
		giftin=0;mnyspt=0;
		while mnyspt<self.gir.mntcst:#if there is more a girl ask for
			self.giftbag.append(lis[giftin])#add into bag
			mnyspt+=lis[giftin].price
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value		#choosy girls like lgift more so...							
			totval+=lis[giftin].value
			giftin+=1
		if mnyspt==0:#this if block is for a very 'poor' boyfriend who had to raise his budget to save his relationship :P
			self.budget+=lis[giftin].price
			self.giftbag.append(lis[giftin])
			mnyspt=lis[giftin].price
			totval+=lis[giftin].value
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value
		self.totvalue=totval
		self.giftbag.append(lis[giftin])
		self.mnyspt=mnyspt				#another attribute for calculating money spent	
	def happinesscalculator(self):
		self.hpns=(self.budget-self.mnyspt)*10/self.budget			#another attribute: happiness	here it is perdeca		
	
class kind(commboy):
	def __init__(self,name,clvrn,sxn,minhotn,budget,gir):
		commboy.__init__(self,name,clvrn,sxn,minhotn,budget,gir)
	
	def giftallocator(self,baske):#here baske is basket type
		self.giftbag=[]#another attribute;committed boy's giftbag
		self.lgiftv=0	#another attribute;this sees total value for luxary gift as liked by choosy girls
		totval=0
		self.mnyspt=0
		
		lis=baske.reversesortasperprice()
		giftin=0;mnyspt=0
		while mnyspt<self.gir.mntcst:
			self.giftbag.append(lis[giftin])
			mnyspt+=lis[giftin].price
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value	
			totval+=lis[giftin].value
			giftin+=1
		if mnyspt==0:#this if block is for a very 'poor' boyfriend who had to raise his budget to save his relationship :P
			self.budget+=lis[giftin].price
			self.giftbag.append(lis[giftin])
			mnyspt=lis[giftin].price
			totval+=lis[giftin].value
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value
		self.totvalue=totval
		self.mnyspt=mnyspt
		
	def happinesscalculator(self):
		self.hpns=self.gir.hpns					#see here it is essential to calculate the girls happiness first
class geek(commboy):
	def __init__(self,name,clvrn,sxn,minhotn,budget,gir):
		commboy.__init__(self,name,clvrn,sxn,minhotn,budget,gir)
	def giftallocator(self,baske):#here baske is basket type
		self.giftbag=[]#another attribute;committed boy's giftbag
		self.lgiftv=0	#another attribute;this sees total value for luxary gift as liked by choosy girls
		totval=0
		self.mnyspt=0
		
		lis=baske.sortasperprice()
		giftin=0;mnyspt=0
		while mnyspt<self.gir.mntcst:
			self.giftbag.append(lis[giftin])
			mnyspt+=lis[giftin].price
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value	
			totval+=lis[giftin].value
			giftin+=1
		if mnyspt==0:#this if block is for a very 'poor' boyfriend who had to raise his budget to save his relationship :P
			self.budget+=lis[giftin].price
			self.giftbag.append(lis[giftin])
			mnyspt=lis[giftin].price
			totval+=lis[giftin].value
			if type(lis[giftin]).__name__=='lgift':
				self.lgiftv+=lis[giftin].value
		left=self.budget-mnyspt
		if left>0:
			for item in lis:
				if type(item).__name__=='lgift' and left>item.price:
					self.giftbag.append(item)
					mnyspt+=item.price
					self.lgiftv+=item.value
					break
		self.totvalue=totval		 
		self.mnyspt=mnyspt
	def happinesscalculator(self):				#see here it is essential to calculate the girls happiness first
		self.hpns=self.gir.smrtn		
