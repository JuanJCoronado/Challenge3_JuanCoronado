import csv
from collections import Counter ##Import Counter for analysis

#csv path of file
csvpath = './Resources/election_data.csv'
csvpath2 = './Resources/election_dataResult.csv'

##VARIABLES CREATION

#For 1st bullet
totalVotes = 0
#For other bullets
CandidateNameList = []

#Loop for reading csv file
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) #skips header
    for x in csvreader:
        #For 1st bullet
        totalVotes = totalVotes + 1
        #Create a candidate name list from third column on csv
        CandidateNameList.append(x[2])

#Create a dictionary from CandidateNamesList that removes duplicates and counts them - from https://datagy.io/python-list-duplicates/
counts = dict(Counter(CandidateNameList))
duplicates = {key:value for key, value in counts.items() if value > 1}

#Update Key to add Percentage in addition to #
#for x in duplicates:
#    print(x)

#Get max key from dictionary - from https://datagy.io/python-get-dictionary-key-with-max-value/
max_key = max(duplicates, key=duplicates.get)

#List to store prints
listStrings = []

#Print results
listStrings.append(['Election Results'])
listStrings.append(['-------------------------'])
listStrings.append([f'Total number of votes: {totalVotes}'])
listStrings.append(['-------------------------'])
listStrings.append([f'{duplicates} are the corresponding votes for each candidate.'])
listStrings.append(['-------------------------'])
listStrings.append([f'Winner is {max_key}'])
listStrings.append(['-------------------------'])

#Output to csv below
with open(csvpath2, 'w', encoding = 'UTF-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for linea in listStrings:
        writer.writerow(linea)