from datetime import date
from tabulate import tabulate
def valid_input(alert):
    valid = False
    while not valid:
        num = input(alert)
        if num.isdigit():
            number = int(num)
            if 0 <= number <= 5:
                return number
            else:
                print("The rating you entered was invalid")
        else:
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

#to get the salary based on the overall rate of each player
def calculate_salary(overall_rate):
    salaryList = [[1,2,3,4], [1000, 700, 500, 400], [80,60,45,30]]
    if overall_rate >= salaryList[2][0]:
        return (salaryList [1][0])
    elif overall_rate < salaryList [2][-1]:
        return (salaryList [1][-1])
    elif overall_rate == salaryList [2][1]:
        return str(salaryList [1][0]) + " " + str(salaryList[1][1])
    for r in range (len(salaryList[2])-1):
        if overall_rate <= salaryList[2][r] and overall_rate > salaryList[2][r+1]:
            return str(salaryList[1][r]) + " " + str(salaryList[1][r+1])

def table_content(playerDetails):
    headers = playerDetails[0].keys()
    rows = [player.values() for player in playerDetails]   
    return tabulate(rows)
    
#to calculate age from player's date of birth
def calculate_age(dateOfBirth):
    dob = date.fromisoformat(dateOfBirth)
    presentDate = date.today()
    age = presentDate.year - dob.year - ((presentDate.month, presentDate.day) < (dob.month, dob.day))
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
                print("The rating you entered was invalid")
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
   
    #headers = playersStat[0].keys() if playersStat else []
    #rows = [player.values() for player in playersStat]
    if playersStat:
        form = '\n'.join([' '.join(map(str, player.values())) for player in playersStat])
        print(form)

    #rows = [[str(value) for value in player.values()] for player in playersStat] # Convert date to string
    #print(tabulate(rows))   

    with open("players.txt", "w") as file:
        file.write(form)

if __name__ == "__main__":
    main()
    