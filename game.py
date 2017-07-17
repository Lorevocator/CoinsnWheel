#!/usr/bin/python3.6

import random
roundcount = 0
counter = 0 
rounds = ["Nevergonnaletyoudown","1st", "2nd", "3rd", "4th", "last"]
curround = 0
coin = ['H','T']
A1 = "?"
B1 = "?"
C1 = "?"
D1 = "?"
AHT = [(coin[random.randrange(0, 2)])]
BHT = [(coin[random.randrange(0, 2)])]
CHT = [(coin[random.randrange(0, 2)])]
DHT = [(coin[random.randrange(0, 2)])]	


def drawcircle():
	global AHT,BHT,CHT,DHT
	global A1,B1,C1,D1	
	firstsec = """\

		           ooo OOO OOO ooo
		       oOO        0        OOo
		   oOO            0            OOo
		oOO               0               OOo
	      oOO                 0                 OOo
	    oOO       A("""
	
	secondsec = """)      0        B("""
	thirdsec = """)    OOo
	   oOO                    0                    OOo
	  oOO                     0                     OOo
	 oOO                      0                      OOo
	 oOO                      0                      OOo
	 oOO000000000000000000000000000000000000000000000OOo
	 oOO                      0                      OOo
	 oOO                      0                      OOo
	  oOO                     0                     OOo
	   oOO        C("""
	fourthsec = """)      0     D("""
	fifthsec = """)         OOo
	    oOO                   0                  OOo
		oOO               0               OOo
		   oOO            0            OOo
		       oOO        0        OOo
		           ooo OOO OOO ooo"""
	print(firstsec,A1, secondsec,B1,thirdsec,C1,fourthsec,D1,fifthsec)


while (AHT == BHT) and (AHT == CHT) and (AHT == DHT): 
	AHT = [(coin[random.randrange(0, 2)])]
	BHT = [(coin[random.randrange(0, 2)])]
	CHT = [(coin[random.randrange(0, 2)])]
	DHT = [(coin[random.randrange(0, 2)])]
tut = input("Do you already know how to play? (y/n) \n")
#print(AHT,BHT,CHT,DHT)
while tut == "n":
	print("The game is simple: \n there's a spinning wheel divided in 4 sections.In each section there is a coin which is either T(ail) or H(ead).\n Your goal is to set them to be all T(ails) or all H(eads). \n In order to do so you can see only two of the coins and turn them over (if you want to) but after your move, the wheel spins and you don't know which of the coins ends up where (of course it only spins so the cicle will be the same). \n Obviously there's a way to always win... \n Good Luck!")
	tut = input("Are you ready to play? (y/n) \n")
if tut == "y":
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
while (AHT != BHT) or (AHT != CHT) or (AHT != DHT): 
	while roundcount < 5:	
		drawcircle()
		roundcount += 1
		print("This is the ",rounds[roundcount]," round!")
		while (counter != 2):
			print("Which coin do you want to see? (A/B/C/D) (",counter,"/ 2 )")
			cointorev = input("")
			counter +=1
			if cointorev == "A" or cointorev == "a":
				if AHT == ['H']:
					A1 = 'H'
				elif AHT == ['T']:
					A1 = 'T'
				drawcircle()
			elif cointorev == "B" or cointorev == "b":
				if BHT == ['H']:
					B1 = 'H'
				elif BHT == ['T']:
					B1 = 'T'
				drawcircle()
			elif cointorev == "C" or cointorev == "c":
				if CHT == ['H']:
					C1 = 'H'
				elif CHT == ['T']:
					C1 = 'T'
				drawcircle()
			elif cointorev == "D" or cointorev == "d":
				if DHT == ['H']:
					D1 = 'H'
				elif DHT == ['T']:
					D1 = 'T'
				drawcircle()				
				
			else:
				print("Please insert a valid coin")
				drawcircle()
				counter -= 1
			#print(AHT,A1,BHT,B1,CHT,C1,DHT,D1)
		if counter == 2:
			counter = 0
	else:
		print("\n\nSorry that was the last round. Try again!")
		quit()
print("Hey you won! https://www.youtube.com/watch?v=1Bix44C1EzY")
























