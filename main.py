from flask import Flask
import pandas as pd
import json

app = Flask(__name__)

# Load the Excel file into a pandas DataFrame
csv_file_path = 'L9HomeworkChallengePlayersInput.csv'
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError as e:
    print(f"FileNotFoundError successfully handled\n"
          f"{e}")
    exit(2)

# Convert the DataFrame to a JSON variable
jsonData = df.to_json(orient='records')
# df is pandas DataFrame object, jsonData is string type,
# we need to convert from "JSON interpreted as string" to useable JSON (jsonFile)
jsonFile = json.loads(jsonData)

# Defining a route to handle the incoming JSON data using GET method
@app.route('/stats/player/<playerFullName>', methods=['GET'])
def process_data(playerFullName):
    playerOriginalName=""
    FTA = 0 #free throws atempted
    FTM = 0 #free throws made
    twoPA = 0 #two points attempted
    twoPM = 0 #two points made
    threePA = 0  #three points attempted
    threePM = 0  #three points made
    REB = 0 #rebounded balls caught
    BLK = 0 #blocked shots
    AST = 0 #assisted shots
    STL = 0 #stolen balls
    TOV = 0 #lost balls

    #babyproof the input of the name, make everything lowercase and without spaces to match with json's PLAYER key
    playerFullName = playerFullName.lower().replace(" ","")
    gamesPlayed = 0

    for player in jsonFile:

        if player["PLAYER"].lower().replace(" ","")==playerFullName:
            playerOriginalName = player["PLAYER"]
            FTA+=player["FTA"]
            FTM+=player["FTM"]
            twoPA+=player["2PA"]
            twoPM+=player["2PM"]
            threePA += player["3PA"]
            threePM += player["3PM"]
            REB+=player["REB"]
            BLK+=player["BLK"]
            AST+=player["AST"]
            STL+=player["STL"]
            TOV+=player["TOV"]
            gamesPlayed+=1

    #In case name is inputted wrongly or that player doesnt exist in database error is raised
    if gamesPlayed == 0:
        return "Error Code 404 - Player not found", 404

    # Create a new JSON extracted from jsonFile
    newJSONData = json.dumps({
        "playerName": playerOriginalName,
        "gamesPlayed": gamesPlayed,
        "traditional": {
            "freeThrows":{
                "attempts": round(FTA/gamesPlayed,1),
                "made": round(FTM/gamesPlayed,1),
                "shootingPercentage": round(FTM/FTA*100,1)
            },
            "twoPoints":{
                "attempts": round(twoPA/gamesPlayed,1),
                "made": round(twoPM/gamesPlayed,1),
                "shootingPercentage": round(twoPM/twoPA*100,1)
            },
            "threePoints":{
                "attempts": round(threePA/gamesPlayed,1),
                "made": round(threePM/gamesPlayed,1),
                "shootingPercentage": round(threePM / threePA * 100, 1)
            },
            "points": round((FTM + 2 * twoPM + 3 * threePM) / gamesPlayed, 1),
            "rebounds": round(REB/gamesPlayed,1),
            "blocks": round(BLK/gamesPlayed,1),
            "assists": round(AST/gamesPlayed,1),
            "steals": round(STL/gamesPlayed,1),
            "turnovers": round(TOV/gamesPlayed,1)
        },
        "advanced":{
            "valorization": round(((FTM + 2*twoPM + 3*threePM + REB + BLK + AST + STL) - (FTA-FTM + twoPA-twoPM + threePA-threePM + TOV))/gamesPlayed  ,1),
            "effectiveFieldGoalPercentage": round((twoPM + threePM + 0.5 * threePM) / (twoPA + threePA) * 100,1),
            "trueShootingPercentage":round((FTM + 2 * twoPM + 3 * threePM) / gamesPlayed*3 / (2 * (twoPA + threePA +0.475 * FTA)) * 100,1),
            "hollingerAssistRatio": round(AST / (twoPA + threePA + 0.475 * FTA + AST + TOV) * 100,1)
        }
    },indent=2)

    return newJSONData,200 , {'Content-Type': 'application/json'}


# App start
if __name__ == '__main__':
    app.run(debug=True)
