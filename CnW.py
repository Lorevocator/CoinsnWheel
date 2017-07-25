#!/usr/bin/python3.6

import random
debug = False
Aname = "A"
Bname = "B"
Cname =	"C"
Dname = "D"
roundcount = 0
counter = 0 
rounds = ["Nevergonnaletyoudown","1st", "2nd", "3rd", "4th", "last"]
curround = 0
coin = ['H','T']
A = "?"
B = "?"
C = "?"
D = "?"
AHT = coin[random.randrange(0, 2)]
BHT = coin[random.randrange(0, 2)]
CHT = coin[random.randrange(0, 2)]
DHT = coin[random.randrange(0, 2)]

simplecir = """\
		           ooo OOO0OOO ooo
		       oOO        0        OOo
		   oOO            0            OOo
		oOO               0               OOo
	      oOO                 0                 OOo
	    oOO                   0                   OOo
	   oOO                    0                    OOo
	  oOO                     0                     OOo
	 oOO                      0                      OOo
	 oOO                      0                      OOo
	 oOO000000000000000000000000000000000000000000000OOo
	 oOO                      0                      OOo
	 oOO                      0                      OOo
	  oOO                     0                     OOo
	   oOO                    0                    OOo
	    oOO                   0                  OOo
	      oOO                 0                 OOo
		oO                0               OOo
		   oOO            0            OOo
		       oOO        0        OOo
		           ooo OOO0OOO ooo"""

def asktoflip(Coin,Coinname):
	flipcoin = 0
	while flipcoin == 0:
		print("Do you want to flip coin",Coinname,"? (y/n)")
		flipit = input("")
		if flipit == "y" or flipit == "Y":
			if Coin == 'H':
				Coin = 'T'
				flipcoin = 1
			elif Coin == 'T':
				Coin = 'H'
				flipcoin = 1
		elif flipit == "n" or flipit == "N":
			flipcoin = 1
		else:
			drawcircle()
			flipcoin = 0
	return Coin
def Highscore():
	try:	
		with open("Highscore.txt") as high:
			score = int(high.read())
			high.close()
		if not score <= roundcount:
			print("New Highscore! \nYour Highscore was",score,"round(s) now is",roundcount,"round(s)")
			newhigh = open("Highscore.txt","w")
			newhigh.write(str(roundcount))
			newhigh.close()					
		else:
			print("Your highscore is",int(score),"round(s). Try harder next time!")
			reset = input("Do you want to reset your Highscore? (y/n)")
			if reset == "y" or reset == "Y":
				print("Your Highscore was resetted! \nBye!") 
				f = open("Highscore.txt","w")
				f.close()
			elif reset == "n" or reset == "N":
			
				try:
					with open("Highscore.txt") as high:
						score = int(high.read())
						high.close()
					print("Ok then! your highscore is still",score,"round(s) !")
				except:
					print("Ok then!")
				finally:
					print("Bye!") 	
	except (FileNotFoundError, ValueError) as error:
		print("New Highscore! \nHighscore is now",roundcount,"round(s)")
		newhigh = open("Highscore.txt","w")
		newhigh.write(str(roundcount))
		newhigh.close()
				
def tutorial():
	print("The game is simple: \nThere's a spinning wheel divided in 4 sections,like this one.")
	print(simplecir)
	input("Press Enter to continue")
	print("\n\nIn each section there is a coin which is either T(ail) or H(ead).")
	drawcircle()
	input("Press Enter to continue\n")
	print("\n\nYour goal is to set them to be all T(ails) or all H(eads). \n ")
	input("Press Enter to continue\n")
	print("\n\nIn order to do so you can see only two of the coins and turn them over (if you want to) but after you see two of the coins, the wheel spins and you don't know which of the coins ends up where .\n\nGood Luck!")

def spin():
	global A,B,C,D,AHT,BHT,CHT,DHT
	if (AHT == BHT) and (AHT== CHT) and (AHT == DHT):
		youwon()
	A = "?"
	B = "?"
	C = "?"
	D = "?"
	times = random.randrange(1,11)
	i = 0
	while i != times:
		AHT,BHT,CHT,DHT = BHT,CHT,DHT,AHT
		i += 1	
def youwon():
	global rounds,roundcount
	print("\n\n\n\nHey you won! https://youtu.be/1Bix44C1EzY \nIt took you ",roundcount,"rounds!")
	Highscore()	
	print("\nThank you! See https://www.github.com/Lorevocator/CoinsnWheel for updates") 
	input("")		
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
	AHT = coin[random.randrange(0, 2)]
	BHT = coin[random.randrange(0, 2)]
	CHT = coin[random.randrange(0, 2)]
	DHT = coin[random.randrange(0, 2)]
	print("There's a 6.25% possibility that this message shows up.")
tut = input("Do you already know how to play? (y/n) \n")

while tut == "n" or tut == "N":
	tutorial()
	tut = input("Are you ready to play? (y/n) \n")
if tut == "d" or tut == "D":
	#enter debug mode
	debug = True
elif tut != "N" and tut != "n":
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
while (AHT != BHT) or (AHT != CHT) or (AHT != DHT): 
	while roundcount < 5:
		if (AHT == BHT) and (AHT == CHT) and (AHT == DHT):
			youwon()
		spin()		
		drawcircle()
		roundcount += 1
		print("This is the ",rounds[roundcount]," round!")
		while (counter != 2):
			if (AHT == BHT) and (AHT== CHT) and (AHT == DHT):
				youwon()
			if debug:
				print(A,B,C,D,AHT,BHT,CHT,DHT)
			print("Which coin do you want to see? (A/B/C/D) (",counter,"/ 2 )")
			cointorev = input("")
			counter +=1
			if cointorev == "A" or cointorev == "a":
				A = AHT
				drawcircle()
				A = asktoflip(A,Aname)
				AHT = A			
				drawcircle()
			elif cointorev == "B" or cointorev == "b":
				B = BHT
				drawcircle()
				B = asktoflip(B,Bname)
				BHT = B
				drawcircle()
			elif cointorev == "C" or cointorev == "c":
				print(CHT)
				C = CHT
				drawcircle()
				C = asktoflip(C,Cname)
				CHT = C
				drawcircle()
			elif cointorev == "D" or cointorev == "d":
				D = DHT
				drawcircle()
				D = asktoflip(D,Dname)
				DHT = D	
				drawcircle()			
			
			else:
				print("Please insert a valid coin")
				drawcircle()
				counter -= 1
			if (AHT == BHT) and (AHT== CHT) and (AHT == DHT):
				youwon()
		if counter == 2:
			counter = 0
	else:
		print("\n\nSorry that was the last round. Try again!")
		print("\nSee https://github.com/Lorevocator/CoinsnWheel for updates")
		input("")
		quit()
























