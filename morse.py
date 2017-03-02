var={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
     'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
     'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
     'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
     'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
     '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
     '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}
etm=[]
mte=[]
def engtomorse():
	sent=raw_input("Enter the text to be encrypted:").split()
	for i in xrange(len(sent)):
		for j in sent[i]:
			etm.append(var[j.upper()])
			etm.append(" ")
		etm.append("  ")

def morsetoeng():
	recieved=raw_input("Enter the Morse code to be decrepted").split("   ")
	#print recieved
	for i in xrange(len(recieved)):
		mte.append(" ")
		tem="".join(recieved[i])
		#print tem
		let=tem.split(" ")
		#print let
		for k in let:
			for key, value in var.iteritems():
    			 if(k==value):
        			mte.append(key)
     	mte.pop(0)
        


def copymorsetoeng():
	recieved=raw_input("Enter the Morse code to be decrepted").split("   ")
	print recieved
	for i in xrange(len(recieved)):
		for j in recieved[i]:
			tem="".join(j)
			
			let=tem.split(" ")
			print let
			for k in let:
				for key, value in var.iteritems():
    				 if(k==value):
        				mte.append(key)
        		

print "Press\n\t1.Convert English to Morse\n\t2.Convert Morse to English"
num=input();
if(num==1):
	engtomorse()
	print "".join(etm)
elif(num==2):
	morsetoeng()
	print "".join(mte)
else:
	print "Please give correct input"

