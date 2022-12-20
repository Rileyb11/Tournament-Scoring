import replit
import time
from prettytable import PrettyTable

x = PrettyTable()


def choice():
  choice = input("Hello, if you would like to play as individuals please enter '1', if you would like to play as teams then please enter '2'")

  if choice == "1":
    indiv()

  elif choice == "2":
    teams()

  else:
    print("Invalid input")
    choice()

def indiv(): # Determines each individual participating
  global indiv1, indiv2, indiv3, indiv4, indiv5, indiv6, indiv7, indiv8, indiv9, indiv10, indiv11, indiv12, indiv13, indiv14, indiv15, indiv16, indiv17, indiv18, indiv19, indiv20
  replit.clear()

  indiv1 = input("Please enter the first individuals name - ")
  indiv2 = input("Please enter the second individuals name - ")
  indiv3 = input("Please enter the third individuals name - ")
  indiv4 = input("Please enter the fourth individuals name - ")
  indiv5 = input("Please enter the fifth individuals name - ")
  indiv6 = input("Please enter the six individuals name - ")
  indiv7 = input("Please enter the seventh individuals name - ")
  indiv8 = input("Please enter the eighth individuals name - ")
  indiv9 = input("Please enter the ninth individuals name - ")
  indiv10 = input("Please enter the tenth individuals name - ")
  indiv11 = input("Please enter the eleventh individuals name - ")
  indiv12 = input("Please enter the twelfth individuals name - ")
  indiv13 = input("Please enter the thirteenth individuals name - ")
  indiv14 = input("Please enter the fourteenth individuals name - ")
  indiv15 = input("Please enter the fifteenth individuals name - ")
  indiv16 = input("Please enter the sixteenth individuals name - ")
  indiv17 = input("Please enter the seventeenth individuals name - ")
  indiv18 = input("Please enter the eighteenth individuals name - ")
  indiv19 = input("Please enter the nineteenth individuals name - ")
  indiv20 = input("Please enter the twentieth individuals name - ")

  indivchoice()

def indivchoice():
  replit.clear()
  ichoice = input("Please enter '1' if you would like to only play one event, or enter '2' if you would like to play multiple events.")

  if ichoice == "1":
    indivsingle()

  elif ichoice == "2":
    indivmulti()

  else: 
    print("Invalid input")
    indivchoice()

def indivsingle():
  replit.clear()
  print("These are the rankings for the mathematics event:")

  x.field_names = ["Individual", "Rank"]

  x.add_row([indiv1, "03"])
  x.add_row([indiv2, "10"])
  x.add_row([indiv3, "18"])
  x.add_row([indiv4, "02"])
  x.add_row([indiv5, "04"])
  x.add_row([indiv6, "12"])
  x.add_row([indiv7, "16"])
  x.add_row([indiv8, "07"])
  x.add_row([indiv9, "09"])
  x.add_row([indiv10, "15"])
  x.add_row([indiv11, "17"])
  x.add_row([indiv12, "11"])
  x.add_row([indiv13, "01"])
  x.add_row([indiv14, "14"])
  x.add_row([indiv15, "19"])
  x.add_row([indiv16, "06"])
  x.add_row([indiv17, "08"])
  x.add_row([indiv18, "20"])
  x.add_row([indiv19, "05"])
  x.add_row([indiv20, "13"])
  x.sortby = "Rank"

  print(x)
  print()

  print("Congrats on coming in first place", indiv13, "!")
  print("Congrats on coming in second place", indiv4, "!")
  print("Congrats on coming in third place", indiv1, "!")

def indivmulti():
  global indiv1score, indiv2score, indiv3score, indiv4score, indiv5score, indiv6score, indiv7score, indiv8score, indiv9score, indiv10score, indiv11score, indiv12score, indiv13score, indiv14score, indiv15score, indiv16score, indiv17score, indiv18score, indiv19score, indiv20score
  replit.clear()
  print ("Individual scoring system:")
  
  x.field_names = ["Individual ranking", "Score"]

  x.add_row(["1st", "100"])
  x.add_row(["2nd", "95"])
  x.add_row(["3rd", "90"])
  x.add_row(["4th", "85"])
  x.add_row(["5th", "80"])
  x.add_row(["6th", "75"])
  x.add_row(["7th", "70"])
  x.add_row(["8th", "65"])
  x.add_row(["9th", "60"])
  x.add_row(["10th", "55"])  
  x.add_row(["11th", "50"])
  x.add_row(["12th", "45"])
  x.add_row(["13th", "40"])
  x.add_row(["14th", "35"])
  x.add_row(["15th", "30"])  
  x.add_row(["16th", "25"])
  x.add_row(["17th", "20"])
  x.add_row(["18th", "15"])
  x.add_row(["19th", "10"])
  x.add_row(["20th", "5"])

  print(x)
  print()
  x.clear()

  x.field_names = ["Individual", "Rank"]

  print("These are the results for the spelling event:")

  x.add_row([indiv1, "03"])
  x.add_row([indiv2, "10"])
  x.add_row([indiv3, "18"])
  x.add_row([indiv4, "02"])
  x.add_row([indiv5, "04"])
  x.add_row([indiv6, "12"])
  x.add_row([indiv7, "16"])
  x.add_row([indiv8, "07"])
  x.add_row([indiv9, "09"])
  x.add_row([indiv10, "15"])
  x.add_row([indiv11, "17"])
  x.add_row([indiv12, "11"])
  x.add_row([indiv13, "01"])
  x.add_row([indiv14, "14"])
  x.add_row([indiv15, "19"])
  x.add_row([indiv16, "06"])
  x.add_row([indiv17, "08"])
  x.add_row([indiv18, "20"])
  x.add_row([indiv19, "05"])
  x.add_row([indiv20, "13"])
  x.sortby = "Rank"

  print(x)
  x.clear_rows()

  print("These are the results for the basketball event:")

  x.add_row([indiv1, "13"])
  x.add_row([indiv2, "05"])
  x.add_row([indiv3, "20"])
  x.add_row([indiv4, "08"])
  x.add_row([indiv5, "06"])
  x.add_row([indiv6, "19"])
  x.add_row([indiv7, "14"])
  x.add_row([indiv8, "01"])
  x.add_row([indiv9, "11"])
  x.add_row([indiv10, "17"])
  x.add_row([indiv11, "15"])
  x.add_row([indiv12, "09"])
  x.add_row([indiv13, "07"])
  x.add_row([indiv14, "16"])
  x.add_row([indiv15, "12"])
  x.add_row([indiv16, "04"])
  x.add_row([indiv17, "02"])
  x.add_row([indiv18, "18"])
  x.add_row([indiv19, "10"])
  x.add_row([indiv20, "03"])
  x.sortby = "Rank"

  print(x)
  x.clear_rows()

  print("These are the results for the science event:")

  x.add_row([indiv1, "15"])
  x.add_row([indiv2, "09"])
  x.add_row([indiv3, "07"])
  x.add_row([indiv4, "16"])
  x.add_row([indiv5, "12"])
  x.add_row([indiv6, "04"])
  x.add_row([indiv7, "02"])
  x.add_row([indiv8, "18"])
  x.add_row([indiv9, "10"])
  x.add_row([indiv10, "03"])
  x.add_row([indiv11, "13"])
  x.add_row([indiv12, "05"])
  x.add_row([indiv13, "20"])
  x.add_row([indiv14, "08"])
  x.add_row([indiv15, "06"])
  x.add_row([indiv16, "19"])
  x.add_row([indiv17, "14"])
  x.add_row([indiv18, "01"])
  x.add_row([indiv19, "11"])
  x.add_row([indiv20, "17"])
  x.sortby = "Rank"

  print(x)
  x.clear_rows()

  print("These are the results for the football event:")

  x.add_row([indiv1, "20"])
  x.add_row([indiv2, "08"])
  x.add_row([indiv3, "13"])
  x.add_row([indiv4, "05"])
  x.add_row([indiv5, "14"])
  x.add_row([indiv6, "01"])
  x.add_row([indiv7, "06"])
  x.add_row([indiv8, "19"])
  x.add_row([indiv9, "15"])
  x.add_row([indiv10, "09"])
  x.add_row([indiv11, "11"])
  x.add_row([indiv12, "17"])
  x.add_row([indiv13, "12"])
  x.add_row([indiv14, "04"])
  x.add_row([indiv15, "07"])
  x.add_row([indiv16, "16"])
  x.add_row([indiv17, "10"])
  x.add_row([indiv18, "03"])
  x.add_row([indiv19, "02"])
  x.add_row([indiv20, "18"])
  x.sortby = "Rank"

  print(x)
  x.clear_rows()

  print("These are the results for the rugby event:")

  x.add_row([indiv1, "10"])
  x.add_row([indiv2, "02"])
  x.add_row([indiv3, "12"])
  x.add_row([indiv4, "07"])
  x.add_row([indiv5, "15"])
  x.add_row([indiv6, "11"])
  x.add_row([indiv7, "03"])
  x.add_row([indiv8, "18"])
  x.add_row([indiv9, "04"])
  x.add_row([indiv10, "09"])
  x.add_row([indiv11, "06"])
  x.add_row([indiv12, "17"])
  x.add_row([indiv13, "08"])
  x.add_row([indiv14, "16"])
  x.add_row([indiv15, "20"])
  x.add_row([indiv16, "19"])
  x.add_row([indiv17, "05"])
  x.add_row([indiv18, "01"])
  x.add_row([indiv19, "13"])
  x.add_row([indiv20, "14"])
  x.sortby = "Rank"

  print(x)
  x.clear()

  indiv1score = 90 + 40 + 30 + 5 + 50
  indiv2score = 55 + 80 + 60 + 65 + 95
  indiv3score = 15 + 20 + 70 + 40 + 45
  indiv4score = 95 + 65 + 25 + 80 + 70
  indiv5score = 85 + 75 + 45 + 25 + 30
  indiv6score = 45 + 10 + 85 + 100 + 50
  indiv7score = 25 + 35 + 95 + 75 + 90
  indiv8score = 70 + 100 + 15 + 10 + 85
  indiv9score = 60 + 50 + 10 + 30 + 85
  indiv10score = 30 + 20 + 90 + 60 + 60
  indiv11score = 20 + 30 + 40 + 50 + 75
  indiv12score = 15 + 60 + 80 + 20 + 20
  indiv13score = 100 + 60 + 5 + 45 + 65
  indiv14score = 35 + 25 + 65 + 85 + 25
  indiv15score = 10 + 45 + 75 + 70 + 5
  indiv16score = 75 + 85 + 10 + 25 + 10
  indiv17score = 65 + 95 + 35 + 55 + 80
  indiv18score = 5 + 15 + 100 + 90 + 100
  indiv19score = 55 + 80 + 55 + 95 + 40
  indiv20score = 40 + 90 + 20 + 15 + 35

  time.sleep(5)
  replit.clear()
  indivfinal()


def indivfinal():

  x.field_names = ["Individual", "Score"]

  x.add_row([indiv1, indiv1score])
  x.add_row([indiv2, indiv2score])
  x.add_row([indiv3, indiv3score])
  x.add_row([indiv4, indiv4score])
  x.add_row([indiv5, indiv5score])
  x.add_row([indiv6, indiv6score])
  x.add_row([indiv7, indiv7score])
  x.add_row([indiv8, indiv8score])
  x.add_row([indiv9, indiv9score])
  x.add_row([indiv10, indiv10score])
  x.add_row([indiv11, indiv11score])
  x.add_row([indiv12, indiv12score])
  x.add_row([indiv13, indiv13score])
  x.add_row([indiv14, indiv14score])
  x.add_row([indiv15, indiv15score])
  x.add_row([indiv16, indiv16score])
  x.add_row([indiv17, indiv17score])
  x.add_row([indiv18, indiv18score])
  x.add_row([indiv19, indiv19score])
  x.add_row([indiv20, indiv20score])
  x.sortby = "Score"
  x.reversesort = True
  print(x)
  x.clear_rows()
  x.clear()

  print("Congrats on coming in first place", indiv2, "!")
  print("Congrats on coming in second place", indiv4, "!")
  print("Congrats on coming in third place", indiv17, "!")

  
def teams(): # Determins each team and the members
  global team1 , team2, team3, team4, team1mem1, team1mem2, team1mem3, team1mem4, team1mem5, team2mem1, team2mem2, team2mem3, team2mem4, team2mem5, team3mem1, team3mem2, team3mem3, team3mem4, team3mem5, team4mem1, team4mem2, team4mem3, team4mem4, team4mem5
  replit.clear()
  
  team1 = input("Please input team 1s name - ")
  team1mem1 = input("Please enter the first member in the team - ")
  team1mem2 = input("Please enter the second member in the team - ")
  team1mem3 = input("Please enter the third member in the team - ")
  team1mem4 = input("Please enter the fourth member in the team - ")
  team1mem5 = input("Please enter the fifth member in the team - ")
  replit.clear()

  team2 = input("Please input team 2s name - ")
  team2mem1 = input("Please enter the first member in the team - ")
  team2mem2 = input("Please enter the second member in the team - ")
  team2mem3 = input("Please enter the third member in the team - ")
  team2mem4 = input("Please enter the fourth member in the team - ")
  team2mem5 = input("Please enter the fifth member in the team - ")
  replit.clear()

  team3 = input("Please input team 3s name - ")
  team3mem1 = input("Please enter the first member in the team - ")
  team3mem2 = input("Please enter the second member in the team - ")
  team3mem3 = input("Please enter the third member in the team - ")
  team3mem4 = input("Please enter the fourth member in the team - ")
  team3mem5 = input("Please enter the fifth member in the team - ")
  replit.clear()

  team4 = input("Please input team 4s name - ")
  team4mem1 = input("Please enter the first member in the team - ")
  team4mem2 = input("Please enter the second member in the team - ")
  team4mem3 = input("Please enter the third member in the team - ")
  team4mem4 = input("Please enter the fourth member in the team - ")
  team4mem5 = input("Please enter the fifth member in the team - ")
  replit.clear()

  x.field_names = [team1, team2, team3, team4]
  
  x.add_row([team1mem1, team2mem1, team3mem1, team4mem1])
  x.add_row([team1mem2, team2mem2, team3mem2, team4mem2])
  x.add_row([team1mem3, team2mem3, team3mem3, team4mem3])
  x.add_row([team1mem4, team2mem4, team3mem4, team4mem4])
  x.add_row([team1mem5, team2mem5, team3mem5, team4mem5])
  
  print("-----------TEAMS-----------")
  print()
  print(x)
  x.clear()
  time.sleep(2)
  
  teamchoice()



def teamchoice(): # Allows user to decide whether they want to play on or multiple events
  replit.clear()
  tchoice = input("Please enter '1' if you would like to only play one event, or enter '2' if you would like to play multiple events.")

  if tchoice == "1":
    teamsingle()

  elif tchoice == "2":
    teammulti()

  else: 
    print("Invalid input")
    teamchoice()

def teamsingle():
  replit.clear()
  print("These are the rankings for the football event:")

  x.field_names = ["Team", "Rank"]

  x.add_row([team1, "3"])
  x.add_row([team2, "1"])
  x.add_row([team3, "2"])
  x.add_row([team4, "4"])
  x.sortby = "Rank"
  print(x)

  print("Congrats on coming in first place", team2, "!")
  print("Congrats on coming in second place", team3, "!")
  print("Congrats on coming in third place", team1, "!")


def teammulti():
  global team1score, team2score, team3score, team4score
  replit.clear()

  y = PrettyTable()
  
  print ("Team scoring system:")
  y.field_names = ["Team ranking", "Score"]

  y.add_row(["1st", "40"])
  y.add_row(["2nd", "30"])
  y.add_row(["3rd", "20"])
  y.add_row(["4th", "10"])

  print(y)
  print()
  y.clear()

  y.field_names = ["Team", "Rank"]
  
  print("These are the results for the spelling event:")

  y.add_row([team1, "1"])
  y.add_row([team2, "4"])
  y.add_row([team3, "3"])
  y.add_row([team4, "2"])
  y.sortby = "Rank"

  print(y)
  y.clear_rows()

  print("These are the results for the basketball event:")

  y.add_row([team1, "3"])
  y.add_row([team2, "2"])
  y.add_row([team3, "1"])
  y.add_row([team4, "4"])
  y.sorby = "Rank"

  print(y)
  y.clear_rows()

  print("These are the results for the science event:")

  y.add_row([team1, "2"])
  y.add_row([team2, "4"])
  y.add_row([team3, "1"])
  y.add_row([team4, "3"])
  y.sortby = "Rank"
  
  print(y)
  y.clear_rows()

  print("These are the results for the football event:")

  y.add_row([team1, "4"])
  y.add_row([team2, "1"])
  y.add_row([team3, "3"])
  y.add_row([team4, "2"])
  y.sortby = "Rank"

  print(y)
  y.clear_rows()

  print("These are the results for the rugby event:")

  y.add_row([team1, "2"])
  y.add_row([team2, "3"])
  y.add_row([team3, "1"])
  y.add_row([team4, "4"])
  y.sortby = "Rank"

  print(y)

  team1score = 40 + 20 + 30 + 10 + 30
  team2score = 10 + 30 + 10 + 40 + 20
  team3score = 20 + 40 + 40 + 20 + 40
  team4score = 30 + 10 + 20 + 20 + 10

  time.sleep(5)
  replit.clear()
  teamfinal()


def teamfinal(): # Displays the final leaderboard based on the scores

  y = PrettyTable()

  print ("These are the total scores of each team:")
  y.field_names = ["Team name", "Score"]

  y.add_row([team1, team1score])
  y.add_row([team2, team2score])
  y.add_row([team3, team3score])
  y.add_row([team4, team4score])
  y.sortby = "Score"
  y.reversesort = True
  print(y)
  y.clear_rows()
  y.clear()

  print()

  print("Congrats on coming in first place", team3, "!")
  print("Congrats on coming in second place", team1, "!")
  print("Congrats on coming in third place", team2, "!")

choice()