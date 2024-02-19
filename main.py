import pandas as pd

#Read .csv file
batData = pd.read_csv('2023 Phillies Batting Data.csv')
rosterData = pd.read_csv('2023 Phillies Season Roster.csv')
uniformData = pd.read_csv('2023 Phillies Uniform Numbers.csv')

#Roster Data - Delete unwanted columns

#Uniform Data - Swap column b with column a
column_change = ['Name', '#']
uniformData = uniformData.reindex(columns=column_change)

#Batting Data - Remove last two rows and all pitcher rows seperately
newBatData = batData.dropna(subset='Pos')
newBatData = newBatData.drop(batData[batData['Pos'] == 'P'].index)

#Add uniform numbers from uniformData to end of rosterData
merge_rost_uni = rosterData.merge(uniformData, how='inner', on='Name')

#Print the updated data
#print(uniformData)
#print(rosterData)
print(merge_rost_uni)

