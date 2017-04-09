import math
class couple:
	def __init__(self,bo,gir):
		self.bo=bo
		self.gir=gir
		self.hpns=bo.hpns+gir.hpns
		self.cmpblty=bo.budget-gir.mntcst+math.fabs(bo.clvrn-gir.smrtn)+math.fabs(bo.sxn-gir.hotn)#these two are added attributes of couple object
