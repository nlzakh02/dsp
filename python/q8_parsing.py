# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

r1 = []
r2 = []
with open('football.csv') as f:
    f.readline()
    for line in f:
        l = line.split(',')
        r1.append([l[0], int(l[5]) - int(l[6])])
        r2.append([l[0], abs(int(l[5]) - int(l[6]))])
print('Smallest difference in ‘for’ and ‘against’ goals:', min(r1, key=lambda r: r[-1])[0])
print('Smallest absolute difference in ‘for’ and ‘against’ goals:', min(r2, key=lambda r: r[-1])[0])
