import csv
StackOverflowCluster = []

with open('survey_results_publicScalesAsNumbers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        tempRow = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        if row['StackOverflowFoundAnswer'] != 'NA' and row['StackOverflowSatisfaction'] != 'NA' and row['StackOverflowCopiedCode'] != 'NA' and row['StackOverflowJobListing'] != 'NA' and row['StackOverflowCompanyPage'] != 'NA' and row['StackOverflowJobSearch'] != 'NA' and row['StackOverflowNewQuestion'] != 'NA' and row['StackOverflowAnswer'] != 'NA' and row['StackOverflowMetaChat'] != 'NA' and row['StackOverflowAdsRelevant'] != 'NA' and row['StackOverflowAdsDistracting'] != 'NA' and row['StackOverflowModeration'] != 'NA' and row['StackOverflowCommunity'] != 'NA' and row['StackOverflowHelpful'] != 'NA' and row['StackOverflowBetter'] != 'NA' and row['StackOverflowWhatDo'] != 'NA' and row['StackOverflowMakeMoney'] != 'NA':
            
            tempRow[0] = int(row['StackOverflowSatisfaction'])
            tempRow[1] = int(row['StackOverflowFoundAnswer'])
            tempRow[2] = int(row['StackOverflowCopiedCode'])
            tempRow[3] = int(row['StackOverflowJobListing'])
            tempRow[4] = int(row['StackOverflowCompanyPage'])
            tempRow[5] = int(row['StackOverflowJobSearch'])
            tempRow[6] = int(row['StackOverflowNewQuestion'])
            tempRow[7] = int(row['StackOverflowAnswer'])
            tempRow[8] = int(row['StackOverflowMetaChat'])
            tempRow[9] = int(row['StackOverflowAdsRelevant'])
            tempRow[10] = int(row['StackOverflowAdsDistracting'])
            tempRow[11] = int(row['StackOverflowModeration'])
            tempRow[12] = int(row['StackOverflowCommunity'])
            tempRow[13] = int(row['StackOverflowHelpful'])
            tempRow[14] = int(row['StackOverflowBetter'])
            tempRow[15] = int(row['StackOverflowWhatDo'])
            tempRow[16] = int(row['StackOverflowMakeMoney'])
            
            

            StackOverflowCluster.append(tempRow)

with open('StackOverflowCluster17Feature.csv', 'wb') as csvfileOut:
    spamwriter = csv.writer(csvfileOut)
    spamwriter.writerow(['StackOverflowSatisfaction','StackOverflowFoundAnswer','StackOverflowCopiedCode'])
    
    
    for x in StackOverflowCluster:
        print(x)
        spamwriter.writerow(x)

                



