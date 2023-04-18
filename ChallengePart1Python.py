import csv
#csv path of file
csvpath = './Resources/budget_data.csv'
csvpath2 = './Resources/budget_dataResult.csv'
##VARIABLES CREATION
#for num 1
totalMonths = 0
#for num 2
totalProfitsLosses = 0
#for num 3
changeNums = []
previousValue = 0
changeSum = 0
avgNum = 0
#for num 4
changeNumsStr = []
maxChange = 0
#for num 5
minChange = 0

with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) #skips header
    for x in csvreader:
        #first number
        totalMonths = totalMonths +1
        #second number
        totalProfitsLosses = totalProfitsLosses + int(x[1])
        #third number
        changeNums.append(int((x[1])) - int(previousValue))
        previousValue = x[1]
        #fourth and fifth numbers
        changeNumsStr.append(x[0])
 
# third number
changeNums.pop(0)
for x in changeNums:
    changeSum = changeSum + x
avgNum = changeSum / len(changeNums)


changeNumsStr.pop(0)
#fourth number
maxChange = max(changeNums)
maxChangeIndex = changeNums.index(maxChange)
MaxChangeStr = changeNumsStr[maxChangeIndex]

#fifth number
minChange = min(changeNums)
minChangeIndex = changeNums.index(minChange)
MinChangeStr = changeNumsStr[minChangeIndex]

#List to save Prints
listStrings = []

listStrings.append(['Financial Analysis test'])
listStrings.append(['----------------------------------'])
listStrings.append([f'Total months: {totalMonths}'])
listStrings.append([f'Total: ${totalProfitsLosses}'])
listStrings.append([f'Average change: ${avgNum}'])
listStrings.append([f'Greater increase in Profits: {MaxChangeStr}, ${maxChange}'])
listStrings.append([f'Greater decrease in Profits: {MinChangeStr}, ${minChange}'])
listStrings.append(['----------------------------------'])

#Output to csv below
with open(csvpath2, 'w', encoding = 'UTF-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for linea in listStrings:
        writer.writerow(linea)