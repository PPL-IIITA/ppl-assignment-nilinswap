import girl
import boy
def girlinputreaderandmaker():#reads from input file and make girl objects.
	filob=open("input.txt",'r')
	st='1'#just so that loop does start at first
	lisg=[] #list of girl objects. ( I din't offend any I.T. feminist)
	while True:
		st=filob.readline()#reads line by line
		if  st=='---\n':# if all input is done for girls this st indicates stop 
			break
		arglis=st.rstrip().split(' ')#rstrip removes end of line and split further splits the string by ' '.returns a list of arguments
		#print("arglis is "+str(arglis))
		name=arglis[0]
		hotn=int(arglis[1])
		smrtn=int(arglis[2])
		mntcst=int(arglis[3])
		choice=arglis[4]
		newg=girl.girl(name,hotn,smrtn,mntcst,choice)
		lisg.append(newg)
	filob.close()
	return lisg

def boyinputreaderandmaker():
	filob=open("input.txt",'r')
	st='1'
	while st!="***\n":			#this is to tell that boy starts from here
		st=filob.readline()
	lisb=[] #list of boy objects. 
	while True:
		st=filob.readline()#reads line by line
		if  st=='---\n':# if all input is done for boy this st indicates stop 
			break
		arglis=st.rstrip().split(' ')#rstrip removes end of line and split further splits the string by ' '.returns a list of arguments
		name=arglis[0]
		clvrn=int(arglis[1])
		sxn=int(arglis[2])
		minhotn=int(arglis[3])
		budget=int(arglis[4])
		newb=boy.boy(name,clvrn,sxn,minhotn,budget)
		lisb.append(newb)
	filob.close()
	return lisb
