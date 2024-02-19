import pandas as pd

#Read .csv file
batData = pd.read_csv('2023 Phillies Batting Data.csv', index_col= 0)
rosterData = pd.read_csv('2023 Phillies Season Roster.csv', index_col=0)
uniformData = pd.read_csv('2023 Phillies Uniform Numbers.csv', index_col=0)

#Roster Data - Delete unwanted columns

#Batting Data - Remove last two rows and all pitcher rows seperately
newBatData = batData.dropna(subset='Pos')
newBatData = newBatData.drop(batData[batData['Pos'] == 'P'].index)

#Add uniform numbers from uniformData to end of rosterData

#Print the updated data
print(rosterData)
