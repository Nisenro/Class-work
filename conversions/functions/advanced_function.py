from datetime import date
from tabulate import tabulate

def valid_input(alert):
    valid = False
    while not valid:
        try:
            num = input(alert)
            number = int(num)
            if 0 <= number <= 5:
                return number
            else:
                print("The rating you entered was invalid")
        except ValueError:
            print("The rating you entered was invalid")
            
def input_playerStat():
    speed = valid_input("")
    shoot =  valid_input("")
    passing = valid_input("")
    defend =  valid_input("")
    dribble =  valid_input("")
    physical =  valid_input("")
    return speed, shoot, passing, defend, dribble, physical
    
def calculate_rating(speed, shoot, passing, defend, dribble, physical):
    total = (speed + shoot + passing + defend + dribble + physical)
    overall_rate = total * 100/30
    return overall_rate

def calculate_salary(overall_rate):
    salaryList = [[1 ,2, 3, 4], [1000, 700, 500, 400], [80, 60, 45, 30]]
    if overall_rate >= salaryList[2][0]:
        return (salaryList [1][0])
    elif overall_rate < salaryList [2][-1]:
        return (salaryList [1][-1])
    elif overall_rate == salaryList [2][1]:
        return str(salaryList [1][0]) + " " + str(salaryList[1][1])
    for r in range (len(salaryList[2])-1):
        if overall_rate <= salaryList[2][r] and overall_rate > salaryList[2][r+1]:
            return str(salaryList[1][r]) + " " + str(salaryList[1][r+1])

def table_content(playersStat):
    headers = playersStat[0].keys()
    rows = [player.values() for player in playersStat]   
    return tabulate(rows, tablefmt='plain')
    
def calculate_age(dateOfBirth):
    dob = date.fromisoformat(dateOfBirth)
    lastYear = date.today().year - 1
    age = lastYear - dob.year - ((date(lastYear, dob.month, dob.day) > date.today()))
    return age, dob

def main():
    playersStat = []
    for numOfPlayer in range(1, 4):
        playerId = input("")
        if playerId == 'end':
            break
        if playerId.isdigit() and (len(playerId) == 2):
            playerName = input("")
            while playerName.isdigit() or not playerName:
                print("The rating you entered was invalid")
                playerName = input("")
                 
            dateOfBirth = input("")
            while (dateOfBirth[4] and dateOfBirth[7] != '-')  or len(dateOfBirth) < 10:
                print("The date you entered was invalid")
                dateOfBirth = input(" ")
                 
            age, dob = calculate_age(dateOfBirth)
            player_stat = input_playerStat()
            overall_rate = calculate_rating(*player_stat)
             
            salary = calculate_salary(overall_rate)
             
            playerDetails = {
             'UID' : playerId,
             'Name': playerName,
             'D.o.B' : dob,
             'Age' : age,
             'Score' : overall_rate,
             'Salary Range' : salary
             
            }
            playersStat.append(playerDetails)
            
        else:
            print("The ID you entered was invalid")
   

    formatted_table = table_content(playersStat)
    print(formatted_table)
    with open("players.txt", "w") as file:
        file.write(formatted_table)

def advanced(filename):
    playersStat = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                player_info = line.strip().split(',')
                playerId, playerName, dateOfBirth = player_info
                age, dob = calculate_age(dateOfBirth)
                player_stat = input_playerStat()
                overall_rate = calculate_rating(*player_stat)
                salary = calculate_salary(overall_rate)
                playerDetails = {
                    'UID': playerId,
                    'Name': playerName,
                    'D.o.B': dob,
                    'Age': age,
                    'Score': overall_rate,
                    'Salary Range': salary
                }
                playersStat.append(playerDetails)
    except FileNotFoundError:
        print("File not found")
        return

    formatted_table = table_content(playersStat)
    print(formatted_table)
    with open("players_advanced.txt", "w") as file:
        file.write(formatted_table)

if __name__ == "__main__":
    filename = "PlayerData.txt"
    advanced(filename)
