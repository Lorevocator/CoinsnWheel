#!/usr/bin/python3.6

import random
roundcount = 0
counter = 0 
rounds = ["Nevergonnaletyoudown","1st", "2nd", "3rd", "4th", "last"]
curround = 0
coin = ['H','T']
A = "?"
B = "?"
C = "?"
D = "?"
AHT = [(coin[random.randrange(0, 2)])]
BHT = [(coin[random.randrange(0, 2)])]
CHT = [(coin[random.randrange(0, 2)])]
DHT = [(coin[random.randrange(0, 2)])]	

def spin():
	global A,B,C,D,AHT,BHT,CHT,DHT
	if (A == B) and (A== C) and (A == D) and (A != "?"):
		youwon()
	A = AHT
	B = BHT
	C = CHT
	D = DHT
	A = "?"
	B = "?"
	C = "?"
	D = "?"
	times = random.randrange(1,11)
	i = 0
	#print(AHT,A,BHT,B,CHT,C,DHT,D)
	while i != times:
		AHT,BHT,CHT,DHT = BHT,CHT,DHT,AHT
		i += 1
		#print(AHT,A,BHT,B,CHT,C,DHT,D)	
def youwon():
	global rounds,roundcount
	print("\n\n\n\nHey you won! https://www.youtube.com/watch?v=1Bix44CEzY\n It took you ",roundcount,"rounds!")
	#restart = input("\nDo you want to try again? (y/n)")
	#if restart == "y":
		
	#if restart == "n":
	print("\nThank you! See github.com/Lorevocator/CoinsnWheel for updates") 		
	quit()

def drawcircle():
	global AHT,BHT,CHT,DHT
	global A,B,C,D	
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
	print(firstsec,A, secondsec,B,thirdsec,C,fourthsec,D,fifthsec)


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
		if (A == B) and (A == C) and (A == D) and (A != "?"):
			youwon()
		spin()		
		drawcircle()
		roundcount += 1
		print("This is the ",rounds[roundcount]," round!")
		while (counter != 2):
			#print(AHT,A,BHT,B,CHT,C,DHT,D)
			if (AHT == BHT) and (AHT== CHT) and (AHT == DHT) and (AHT != "?"):
				youwon()
			print("Which coin do you want to see? (A/B/C/D) (",counter,"/ 2 )")
			cointorev = input("")
			counter +=1
			if cointorev == "A" or cointorev == "a":
				if AHT == ['H']:
					A = 'H'
				elif AHT == ['T']:
					A = 'T'
				drawcircle()				
				var = 0
				while var == 0:
					print("Do you want to flip coin A? (y/n)")
					flipit = input("")
					if flipit == "y":
						if A == 'H':
							A = 'T'
							AHT = ['T']
							var = 1
						elif A == 'T':
							A = 'H'
							AHT = ['H']
							var = 1
					elif flipit == "n" or flipit == "N":
						var = 1
					else:
						drawcircle()
						var = 0
				drawcircle()
			elif cointorev == "B" or cointorev == "b":
				if BHT == ['H']:
					B = 'H'
				elif BHT == ['T']:
					B = 'T'
				drawcircle()
				var = 0
				while var == 0:
					print("Do you want to flip coin B? (y/n)")
					flipit = input("")
					if flipit == "y" or flipit == "Y":
						if B == 'H':
							B = 'T'
							BHT = ['T']
							var = 1
						elif B == 'T':
							B = 'H'
							BHT = ['H']
							var = 1
					elif flipit == "n" or flipit == "N":
						var = 1
					else:
						drawcircle()
						var = 0
				drawcircle()
			elif cointorev == "C" or cointorev == "c":
				if CHT == ['H']:
					C = 'H'
				elif CHT == ['T']:
					C = 'T'
				drawcircle()
				var = 0
				while var == 0:
					print("Do you want to flip coin C? (y/n)")
					flipit = input("")
					if flipit == "y" or flipit == "Y":
						if C == 'H':
							C = 'T'
							CHT = ['T']
							var = 1
						elif C == 'T':
							C = 'H'
							CHT = ['H']
							var = 1
					elif flipit == "n" or flipit == "N":
						var = 1
					else:
						drawcircle()
						var = 0
				drawcircle()
			elif cointorev == "D" or cointorev == "d":
				if DHT == ['H']:
					D = 'H'
				elif DHT == ['T']:
					D = 'T'
				drawcircle()
				var = 0
				while var == 0:
					print("Do you want to flip coin D? (y/n)")
					flipit = input("")
					if flipit == "y" or flipit == "Y":
						if D == 'H':
							D = 'T'
							DHT = ['T']
							var = 1
						elif D == 'T':
							D = 'H'
							DHT = ['H']
							var = 1
					elif flipit == "n" or flipit == "N":
						var = 1
					else:
						drawcircle()
						var = 0	
				drawcircle()			
			
			else:
				print("Please insert a valid coin")
				drawcircle()
				counter -= 1
			if (AHT == BHT) and (AHT== CHT) and (AHT == DHT) and (AHT != "?"):
				youwon()
			##print(AHT,A,BHT,B,CHT,C,DHT,D)
		if counter == 2:
			counter = 0
	else:
		print("\n\nSorry that was the last round. Try again!")
		quit()
print("Hey you won! https://www.youtube.com/watch?v=1Bix44CEzY")
























