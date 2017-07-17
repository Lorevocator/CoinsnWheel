#!/usr/bin/python3.6

import random

sep = ' '
rounds = [1, 2, 3, 4, 5]
curround = 0
coin = ['H', 'T']
rou
A1 = [(coin[random.randrange(0, 2)])]
B1 = [(coin[random.randrange(0, 2)])]
C1 = [(coin[random.randrange(0, 2)])]
D1 = [(coin[random.randrange(0, 2)])]

turn = [random.randrange(1, 5), random.randrange(1, 5), random.randrange(1, 5), random.randrange(1, 5), random.randrange(1, 5)]

def drawcircle():
	firstsec = """\

		           ooo OOO OOO ooo
		       oOO        0        OOo
		   oOO            0            OOo
		oOO               0               OOo
	      oOO                 0                 OOo
	    oOO       A"""
	
	secondsec = """         0        """
	print("Round = "round firstsec, secondsec)


while (A1 != B1) and (A1 != C1) and (A1 != D1): 
	A1 = [(coin[random.randrange(0, 2)])]
	B1 = [(coin[random.randrange(0, 2)])]
	C1 = [(coin[random.randrange(0, 2)])]
	D1 = [(coin[random.randrange(0, 2)])]
tut = input("Do you already know how to play? (y/n) \n")
while tut == "n":
	print("The game is simple: \n there's a spinning wheel divided in 4 sections.In each section there is a coin which is either T(ail) or H(ead).\n Your goal is to set them to be all T(ails) or all H(eads). \n In order to do so you can see only two of the coins and turn them over (if you want to) nut after your move the wheel spins and you don't know which of the coins ends up where (of course it only spins so the cicle will be the same). \n Obviusly there's a way to always win... \n Good Luck!")
	tut = input("Are you ready to play? (y/n) \n")

while (A1 != B1) or (A1 != C1) or (A1 != D1): 
	circle = """\
	
		           ooo OOO OOO ooo
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
	    oOO                   0                   OOo
	      oOO                 0                 OOo
		oO                0               OOo
		   oOO            0            OOo
		       oOO        0        OOo
		           ooo OOO OOO ooo
	"""
	print(circle)
	drawcircle()
	input("")
	break






















