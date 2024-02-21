import pandas as pd

#Read .csv file
batData = pd.read_csv('2023 Phillies Batting Data.csv')
rosterData = pd.read_csv('2023 Phillies Season Roster.csv')
uniformData = pd.read_csv('2023 Phillies Uniform Numbers.csv')

#Roster Data - Delete unwanted columns
newRosterData = rosterData.drop(['Unnamed: 2', 'Ht', 'Wt', 'DoB', 'WAR', 'Unnamed: 28'], axis=1)

#Uniform Data - Swap column b with column a
column_change = ['Name', '#']
uniformData = uniformData.reindex(columns=column_change)

#Batting Data - Remove last two rows and all pitcher rows seperately, add 'b-' to all column name prefix, clean up
newBatData = batData.dropna(subset='Pos')
newBatData = newBatData.drop(batData[batData['Pos'] == 'P'].index)

newBatData = newBatData.drop(['Rk', 'Age', 'OPS+', 'GDP', 'HBP', 'SH', 'SF', 'IBB', 'Name-additional'], axis=1)


newBatData = newBatData.add_prefix('b-')
newBatData = newBatData.rename(columns={'b-Pos': 'Pos', 'b-Name': 'Name'})

#Add uniform numbers from uniformData to end of rosterData, and add bat data
merge_rost_uni = newRosterData.merge(uniformData, how='inner', on='Name')
merge_rost_uni = newRosterData.merge(newBatData, how='inner', on='Name')

#Rename new rosterData columns
merge_rost_uni = merge_rost_uni.rename(columns={'#': 'Uniform#'})

#Export data as a .csv in folder

#   TEST AREA
#print(rosterData)
#pd.options.display.max_columns = None
print(merge_rost_uni.keys())
# test = merge_rost_uni[['Name', 'Age', 'B', 'T']]
print(merge_rost_uni[:4])

