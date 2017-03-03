var={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
     'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
     'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
     'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
     'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
     '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
     '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','.':'.-.-.-','?':'..--..',
     '=':'-...-','\'':'--..--','/':'-..-.','@':'.--.-.'}
etm=[]
mte=[]
etmaudio=[]
def audmorse():
	from pydub import AudioSegment
	sound1=AudioSegment.from_file("dot.wav")
	sound2=AudioSegment.from_file("dash.wav")
	space=AudioSegment.from_file("space.wav")
	leng=len(space)
	#print leng
	space=space[-250:]
	sound=sound1[-1:]
	

	for i in range(len(etm)):
		for j in etm[i]:
			etmaudio.append(j)

	for i in etmaudio:
		if(i=='-'):
			temp=sound+sound2
			sound=temp
		elif(i=='.'):
			temp=sound+sound1
			sound=temp
		elif(i==' '):
			temp=sound+space
			sound=temp
	file_handle = sound.export("morseaudio.mp3", format="mp3")

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

print "Press\n\t1.Convert English to Morse\n\t2.Convert Morse to English"
num=input();
if(num==1):
	engtomorse()
	audmorse()
	print "".join(etm)
	#print etm
elif(num==2):
	morsetoeng()
	print "".join(mte)
else:
	print "Please give correct input"




