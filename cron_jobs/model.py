#!/bin/sh

import pandas as pd
import numpy as np

import lightgbm as lgb
from sklearn import metrics
from sklearn.metrics import (
    confusion_matrix, 
    accuracy_score, 
    precision_recall_curve,
    average_precision_score,
    roc_curve,
    roc_auc_score,
    classification_report,
    plot_confusion_matrix
)
from sklearn.model_selection import train_test_split

from datetime import date
import re
from datetime import datetime,timedelta
import requests
import json

import treon
import unittest
import pickle

# Importation of Revised Dataset from April 10th, 2022
df = pd.read_csv("/Users/matthewbuttlerives/Desktop/Data Folder/Period_1_Game_Stats_Final_ModelReady(April-10th-2022).csv")

# Split data
y = df.pop('won')
X = df

# Split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

# Get today's date
today = date.today()

# dd/mm/YY
Day = today.strftime("%d")
Month = today.strftime("%m")
Year = today.strftime("%Y")
today = date.today()
print("Today's date:", today)

# Get API info
response = requests.get(("https://api.sportradar.us/nhl/trial/v7/en/games/{Year}/{Month}/{Day}/schedule.json?api_key=sa8b3wuwy549qwy6jw6srsgv").format(Day=Day, Month = Month, Year = Year))

# Set response as json
x = response.json()

# Print API info
def getrs(obj):
    Todays_Schedule = []
    Todays_Schedule = pd.DataFrame([],columns = ["Game ID","Home Team",'Home Team ID',"Away Team","Away Team ID","Start Time"])
    q = len(obj["games"])
    for i in range(q):
            GID = obj["games"][i]["id"]
            H = obj['games'][i]['home']['name']
            Hid = obj['games'][i]['home']['id']
            A = obj['games'][i]['away']['name']
            Aid = obj['games'][i]['away']['id']
            PD = obj['games'][i]['scheduled']
            PD = re.search('T(.+?)Z',PD)
            if PD:
                found = PD.group(1)
            format = "%H:%M:%S"
            d = datetime.strptime(found,format) - timedelta(hours=4)
            d = d.strftime("%H:%M:%S")
            PD = d
            temp_df = [GID,H,Hid,A,Aid,PD]
            a_series = pd.Series(temp_df,index = Todays_Schedule.columns)
            Todays_Schedule = Todays_Schedule.append(a_series, ignore_index=True)
    return Todays_Schedule
data=getrs(x)
data.head(20)

# Define function to generate stats from the first period of play
def Game_Home_Team_Stats(game_id,home_team_id,game_time):
    ts = 0
    tsa = 0
    go = 0
    goa = 0
    t = 0
    ta = 0
    h = 0
    ha = 0
    bs = 0
    bsa = 0
    gi = 0
    gia = 0
    ms = 0
    msa = 0
    p = 0
    pa = 0
    tfw = 0
    tfl = 0
    away = 0
    home = 0
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time < game_time:
        pass
    else:
        response = requests.get(("https://api.sportradar.us/nhl/trial/v7/en/games/{obj}/pbp.json?api_key=sa8b3wuwy549qwy6jw6srsgv").format(obj = game_id))
        x = response.json()
        y = len(x['periods'][0]['events'])
        htc = x['home']['id']
        Team_Name = x['home']['name']
        Away_Name = x['away']['name']
        if htc == home_team_id:
            home = 1
        else:
            away = 1
        for i in range(y):
            j = x['periods'][0]['events'][i]['event_type']
            if j == 'faceoff':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                        tfw = tfw + 1
                else:
                        tfl = tfl + 1
            elif j == 'goal':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                        go = go + 1
                else:
                    goa = goa + 1
            elif j == 'penalty':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                    p = p + 1
                else:
                    pa = pa + 1
            elif j == 'shotmissed' and 'blocked' in x['periods'][0]['events'][i]['description']:
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                        bs = bs + 1
                else:
                        bsa = bsa + 1
            elif j == 'shotmissed' and 'missed' in x['periods'][0]['events'][i]['description']:
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                        ms = ms + 1
                else:
                        msa = msa + 1
            elif j == 'giveaway':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                    gi = gi + 1
                else:
                    gia = gia + 1
            elif j == 'hit':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                    h = h + 1
                else:
                    ha = ha + 1
            elif j == 'takeaway':
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                    t = t + 1
                else:
                    ta = ta + 1
            elif 'shot' in j:
                team_id = x['periods'][0]['events'][i]['attribution']['id']
                if team_id == home_team_id:
                    ts = ts + 1
                else:
                    tsa = tsa + 1
            else:
                pass
            d = {"Team_Name":[Team_Name],"shots": [ts], "shots_against": [tsa],"goals":[go],"goals_against":[goa],"takeaways":[t],"takeaways_against":[ta],"hits":[h],"hits_against":[ha],"blockedShots":[bs],"blockedShots_against":[bsa],"giveaways":[gi],"giveaways_against":[gia],"missedShots":[ms],"missedShots_against":[msa],"penalties":[p],"penalties_against":[pa],"#Won Faceoffs":[tfw],"#Lost Faceoffs":[tfl],'HoA_away':[away],'HoA_home':[home]}
            da = {"Team_Name":[Away_Name],"shots": [tsa], "shots_against": [ts],"goals":[goa],"goals_against":[go],"takeaways":[ta],"takeaways_against":[t],"hits":[ha],"hits_against":[h],"blockedShots":[bsa],"blockedShots_against":[bs],"giveaways":[gia],"giveaways_against":[gi],"missedShots":[msa],"missedShots_against":[ms],"penalties":[pa],"penalties_against":[p],"#Won Faceoffs":[tfl],"#Lost Faceoffs":[tfw],'HoA_away':[home],'HoA_home':[away]}
            Home_Team_Stats = pd.DataFrame(d)
            Away_Team_Stats = pd.DataFrame(da)
            #series_obj = pd.Series(da)
            # Add a series as a row to the dataframe  
            All_Team_Stats = Home_Team_Stats.append(Away_Team_Stats,ignore_index=True)
        return All_Team_Stats
    
# Define function that takes tonights schedule (containing the nessecary Unique Id's) to gather the correct statistics from sportsradar
def get_game_stats(obj):
    c = ["Team_Name","shots", "shots_against","goals","goals_against","takeaways","takeaways_against","hits","hits_against","blockedShots","blockedShots_against","giveaways","giveaways_against","missedShots","missedShots_against","penalties","penalties_against","#Won Faceoffs","#Lost Faceoffs",'HoA_away','HoA_home']
    Tonights_games_stats = pd.DataFrame([],columns = c)
    r = len(obj['Game ID'])
    for i in range(r):
        game_id = obj['Game ID'][i]
        home_team_id = obj['Home Team ID'][i]
        game_start = obj['Start Time'][i]
        temp_df = Game_Home_Team_Stats(game_id,home_team_id,game_start)
        Tonights_games_stats = Tonights_games_stats.append(temp_df,ignore_index = True)
    return Tonights_games_stats

# Define function that inserts statistics for all of tonights teams into LGBMmodel
def tonights_bets(obj):
    m = len(obj)
    for i in range(m):
        Game_y_pred = final_model.predict(X_Game_test)
        prediction = [round(value) for value in Game_y_pred]
        print(prediction)
        probability = final_model.predict_proba(X_Game_test)
        print(probability)
tonights_data=get_game_stats(data)

# Generate Predictions from LGBMmodel
m = len(tonights_data)
y = tonights_data.pop('Team_Name')
for i in range(m):
    x_value = tonights_data.iloc[i]
    test = np.array([x_value])
    x_value = test.reshape(1, -1)
    Game_y_pred = final_model.predict(x_value)
    prediction = [round(value) for value in Game_y_pred]
    probability = final_model.predict_proba(x_value)

# Split data
y = df.pop('won')
X = df

# Split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

# Final Lightgbm.LGBMClassifier model
final_model = lgb.LGBMClassifier(learning_rate=0.04, max_depth=10, num_leaves = 31, random_state=42)
final_model.fit(X_train,y_train)

with open('classifier.pkl', 'wb') as files:
    pickle.dump(model, files)