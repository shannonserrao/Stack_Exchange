import csv
StackOverflowCluster = []

with open('survey_results_public.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        tempRow = [0,0,0,0,0,0,0,0,0]
        
        if row['StackOverflowFoundAnswer'] != 'NA' and row['StackOverflowSatisfaction'] != 'NA' and row['StackOverflowCopiedCode'] != 'NA' and row['StackOverflowJobListing'] != 'NA' and row['StackOverflowCompanyPage'] != 'NA' and row['StackOverflowJobSearch'] != 'NA' and row['StackOverflowNewQuestion'] != 'NA' and row['StackOverflowAnswer'] != 'NA' and row['StackOverflowMetaChat'] != 'NA' :
            
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

            if row['StackOverflowJobListing'] == 'Haven\'t done at all':
                tempRow[3] = 2
            elif row['StackOverflowJobListing'] == 'Once or twice':
                tempRow[3] = 4
            elif row['StackOverflowJobListing'] == 'Several times':
                tempRow[3] = 6
            elif row['StackOverflowJobListing'] == 'At least once each week':
                tempRow[3] = 8
            elif row['StackOverflowJobListing'] == 'At least once each day':
                tempRow[3] = 10

            if row['StackOverflowCompanyPage'] == 'Haven\'t done at all':
                tempRow[4] = 2
            elif row['StackOverflowCompanyPage'] == 'Once or twice':
                tempRow[4] = 4
            elif row['StackOverflowCompanyPage'] == 'Several times':
                tempRow[4] = 6
            elif row['StackOverflowCompanyPage'] == 'At least once each week':
                tempRow[4] = 8
            elif row['StackOverflowCompanyPage'] == 'At least once each day':
                tempRow[4] = 10

            if row['StackOverflowJobSearch'] == 'Haven\'t done at all':
                tempRow[5] = 2
            elif row['StackOverflowJobSearch'] == 'Once or twice':
                tempRow[5] = 4
            elif row['StackOverflowJobSearch'] == 'Several times':
                tempRow[5] = 6
            elif row['StackOverflowJobSearch'] == 'At least once each week':
                tempRow[5] = 8
            elif row['StackOverflowJobSearch'] == 'At least once each day':
                tempRow[5] = 10

            if row['StackOverflowNewQuestion'] == 'Haven\'t done at all':
                tempRow[6] = 2
            elif row['StackOverflowNewQuestion'] == 'Once or twice':
                tempRow[6] = 4
            elif row['StackOverflowNewQuestion'] == 'Several times':
                tempRow[6] = 6
            elif row['StackOverflowNewQuestion'] == 'At least once each week':
                tempRow[6] = 8
            elif row['StackOverflowNewQuestion'] == 'At least once each day':
                tempRow[6] = 10

            if row['StackOverflowAnswer'] == 'Haven\'t done at all':
                tempRow[7] = 2
            elif row['StackOverflowAnswer'] == 'Once or twice':
                tempRow[7] = 4
            elif row['StackOverflowAnswer'] == 'Several times':
                tempRow[7] = 6
            elif row['StackOverflowAnswer'] == 'At least once each week':
                tempRow[7] = 8
            elif row['StackOverflowAnswer'] == 'At least once each day':
                tempRow[7] = 10

            if row['StackOverflowMetaChat'] == 'Haven\'t done at all':
                tempRow[8] = 2
            elif row['StackOverflowMetaChat'] == 'Once or twice':
                tempRow[8] = 4
            elif row['StackOverflowMetaChat'] == 'Several times':
                tempRow[8] = 6
            elif row['StackOverflowMetaChat'] == 'At least once each week':
                tempRow[8] = 8
            elif row['StackOverflowMetaChat'] == 'At least once each day':
                tempRow[8] = 10

            StackOverflowCluster.append(tempRow)

with open('StackOverflowCluster9Feature.csv', 'wb') as csvfileOut:
    spamwriter = csv.writer(csvfileOut)
    spamwriter.writerow(['StackOverflowSatisfaction','StackOverflowFoundAnswer','StackOverflowCopiedCode'])
    
    
    for x in StackOverflowCluster:
        print(x)
        spamwriter.writerow(x)

                



