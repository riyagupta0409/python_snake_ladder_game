from os import system,name
import sys
import random

system("color")
COLOR = {
    "Bold":"\033[1m",
    "Dim":"\033[2m",
    "Underlined":"\033[4m",
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "YELLOW":"\033[33m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",   # # color-off
    "PURPLE":"\033[0;35m",
    "CYAN": "\033[0;36m"
}

def clear():
	if name == "nt":
		_=system('cls')
	else:
		_=system('clear')

ladders ={"03":"22","09":"34","11":"49","17":"90","24":"94","39":"96","63":"81"}
snakes = {"99":"05","91":"64","89":"17","70":"47","62":"38","50":"12","59":"19"}

# variables 
player1 = 0
player2 = 0
turn = 1

def check_state(position):
	if position > 100:
		print("CAN'T MAKE MOVE")
		return -1
	if position == 100:
		return 101
	position_s = str(position).rjust(2,'0') 
	if position_s in ladders.keys():
		print("PLAYER PROMOTED BY LADDER FROM",position_s,"TO",ladders[position_s])
		return int(ladders[position_s])
	if position_s in snakes.keys():
		print("PLAYER DEMOTED BY SNAKE FROM",position_s,"TO",snakes[position_s])
		return int(snakes[position_s])
	else:
		return position 


def make_move():
	global turn
	global player1
	global player2
	player = turn 
	current_playing_player = "PLAYER1" if turn==1 else "PLAYER2"
	player_standing = player1 if turn==1 else player2
	print("CURRENT TURN :-  " , current_playing_player)
	move = input("ENTER ANY KEY TO ROLL DICE  ")
	roll_dice = random.randint(1, 6)
	print("DICE SHOWS" , roll_dice)
	# move = input("ENTER ANY KEY TO MAKE MOVE  ")
	ans = check_state(roll_dice + player_standing)
	if ans == -1:
		ans = player_standing
	if ans == 101:
		print(current_playing_player,"WON")
		sys.exit()
	else:
		player_standing = ans
		if turn == 1:
			player1 = player_standing
		else:
			player2 = player_standing
		turn = 2 if player ==1 else 1


		move = input("ENTER ANY KEY TO MAKE CHANGES ON BOARD  ")
		print_table()


def print_table():
	clear()
	change = 0
	global player1
	global player2
	num = 101
	for i in range(10):
		print('\n')
		if change == 0:			
			for j in range(10):
				num = int(num)
				num-=1
				num = str(num).rjust(2,'0')
				if num == "100":
					print(num , end="   ")
					continue
				if num in ladders.keys():
					print(COLOR["GREEN"],num,COLOR["ENDC"],end="    ",sep="")
				elif num in snakes.keys():
					print(COLOR["RED"],num,COLOR["ENDC"],end="    ",sep="")
				elif num == str(player1).rjust(2,'0') and num == str(player2).rjust(2,'0'):
					print(COLOR["PURPLE"],num,COLOR["ENDC"],end="    ",sep="")
					continue
				elif num == str(player1).rjust(2,'0'):
					print(COLOR["BLUE"],num,COLOR["ENDC"],end="    ",sep="")
				elif num == str(player2).rjust(2,'0'):
					print(COLOR["YELLOW"],num,COLOR["ENDC"],end="    ",sep="")
				else:
					print(num,end="    ")
			change = 1
			continue
		else:
			num = int(num)
			for j in range(num - 9,num+1):
				j-=1
				j = str(j).rjust(2,'0')
				if j == "100":
					print(j , end="   ")
					continue
				if j in ladders.keys():
					print(COLOR["GREEN"],j,COLOR["ENDC"],end="    ",sep="")
				elif j in snakes.keys():
					print(COLOR["RED"],j,COLOR["ENDC"],end="    ",sep="")
				elif j == str(player1).rjust(2,'0') and j == str(player2).rjust(2,'0'):
					print(COLOR["PURPLE"],j,COLOR["ENDC"],end="    ",sep="")
					continue
				elif j == str(player1).rjust(2,'0'):
					print(COLOR["BLUE"],j,COLOR["ENDC"],end="    ",sep="")
				elif j == str(player2).rjust(2,'0'):
					print(COLOR["YELLOW"],j,COLOR["ENDC"],end="    ",sep="")
				else:
					print(j,end="    ")
			num-=10
			change = 0
	print('\n\n')
	make_move()


def first_window():
	print("PLAYER 1 is in blue color")
	print("PLAYER 2 is in yellow color")
	print("Ladders are shown in GREEN color and their path is hidden")
	print("snakes  are shown in RED color and their path is hidden")
	print("If players are at same position then it will be shown in PURPLE")
	start = input("Press any key to start ")
	print_table()


first_window()