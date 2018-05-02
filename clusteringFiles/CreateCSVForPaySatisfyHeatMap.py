import csv
regionBySatisfyByMoney = []
for i in range(11):
    regionBySatisfyByMoney.append([0,0,0,0,0,0,0,0,0,0,0,0,0])
with open('survey_results_public.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row['Country'], row['JobSatisfaction'], row['Salary'])
        if row['Country'] == 'United States' and row['JobSatisfaction'] != 'NA' and row['Salary'] != 'NA':
            if float(row['Salary'])> 10000 and float(row['Salary']) <= 30000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][1] += 1
            elif float(row['Salary']) > 30000 and float(row['Salary']) <= 50000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][2] += 1
            elif float(row['Salary']) > 50000 and float(row['Salary']) <= 70000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][3] +=1
            elif float(row['Salary']) > 70000 and float(row['Salary']) <= 90000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][4] +=1
            elif float(row['Salary']) > 90000 and float(row['Salary']) <= 110000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][5] +=1
            elif float(row['Salary']) > 110000 and float(row['Salary']) <= 130000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][6] +=1
            elif float(row['Salary']) > 130000 and float(row['Salary']) <= 150000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][7] +=1
            elif float(row['Salary']) > 150000 and float(row['Salary']) <= 170000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][8] +=1
            elif float(row['Salary']) > 170000 and float(row['Salary']) <= 190000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][9] +=1
            elif float(row['Salary']) > 190000 and float(row['Salary']) <= 210000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][10] +=1
            elif float(row['Salary']) > 210000 and float(row['Salary']) <= 230000:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][11] +=1
            elif float(row['Salary']) > 230000 :
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][12] +=1
            else:
                regionBySatisfyByMoney[int(row['JobSatisfaction'])][0] +=1
print(regionBySatisfyByMoney)

with open('SalaryBySatisfactionMoreGroups.csv', 'wb') as csvfileOut:
    spamwriter = csv.writer(csvfileOut)
    
    for x in range(11):
        print(regionBySatisfyByMoney[x])
        spamwriter.writerow(regionBySatisfyByMoney[x])
