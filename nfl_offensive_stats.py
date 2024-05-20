"""
open the csv file called "nfl_offensive_stats.csv" and
read in the csv data from the file
"""
# import the csv module
import csv
# open the csv file
with open('nfl_offensive_stats.csv', 'r') as f:
    # read the csv data
    data = list(csv.reader(f))
"""
the 3rd column in data is player position, the fourth column
is the player, and the 8th column is the passing yards.
For each player whose position in column 3 is "QB",
determine the sum of yards from column 8
"""
# create a dictionary to hold the player name and passing yards
passing_yards = {}
# loop through the data
for row in data:
    # check if the player is a quarterback
    if row[2] == 'QB':
        # check if the player is already in the dictionary
        if row[3] in passing_yards:
            # add the passing yards to the existing value
            passing_yards[row[3]] += int(row[7])
        else:
            # add the player to the dictionary
            passing_yards[row[3]] = int(row[7])
"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
"""
for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
    print(player, passing_yards[player])
    
""" 
In the data we just read in, the fourth column is the player
and the 8th column is the passing yards. Get the sum of 
yards from column 8 where the 4th column value is
"Aaron Rodgers"
"""
# create a variable to hold the sum of passing yards for Aaron Rodgers
aaron_rodgers_yards = 0
# loop through the data
for row in data:
    # check if the player is Aaron Rodgers
    if row[3] == 'Aaron Rodgers':
        # add the passing yards to the sum
        aaron_rodgers_yards += int(row[7])
# print the sum of passing yards for Aaron Rodgers
print(f"Aaron rodger's yards: {aaron_rodgers_yards}")


