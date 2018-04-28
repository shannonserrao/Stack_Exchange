import csv
StackOverflowCluster = []

with open('survey_results_public.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        tempRow = [0,0,0]
        
        if row['StackOverflowFoundAnswer'] != 'NA' and row['StackOverflowSatisfaction'] != 'NA' and row['StackOverflowCopiedCode'] != 'NA':
            
            tempRow[0] = int(row['StackOverflowSatisfaction'])
            if row['StackOverflowFoundAnswer'] == 'Haven\'t done at all':
                tempRow[1] = 2
            elif row['StackOverflowFoundAnswer'] == 'Once or twice':
                tempRow[1] = 4
            elif row['StackOverflowFoundAnswer'] == 'Several times':
                tempRow[1] = 6
            elif row['StackOverflowFoundAnswer'] == 'At least once each week':
                tempRow[1] = 8
            elif row['StackOverflowFoundAnswer'] == 'At least once each day':
                tempRow[1] = 10
            if row['StackOverflowCopiedCode'] == 'Haven\'t done at all':
                tempRow[2] = 2
            elif row['StackOverflowCopiedCode'] == 'Once or twice':
                tempRow[2] = 4
            elif row['StackOverflowCopiedCode'] == 'Several times':
                tempRow[2] = 6
            elif row['StackOverflowCopiedCode'] == 'At least once each week':
                tempRow[2] = 8
            elif row['StackOverflowCopiedCode'] == 'At least once each day':
                tempRow[2] = 10
            StackOverflowCluster.append(tempRow)

with open('StackOverflowCluster3Feature.csv', 'wb') as csvfileOut:
    spamwriter = csv.writer(csvfileOut)
    spamwriter.writerow(['StackOverflowSatisfaction','StackOverflowFoundAnswer','StackOverflowCopiedCode'])
    
    
    for x in StackOverflowCluster:
        print(x)
        spamwriter.writerow(x)

                



