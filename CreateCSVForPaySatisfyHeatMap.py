import csv
regionBySatisfyByMoney = []
for i in range(7):
    regionBySatisfyByMoney.append([0,0,0,0,0,0,0,0,0,0,0])
with open('survey_results_public.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print row['Country'], row['JobSatisfaction'], row['Salary']
        if row['Country'] == 'United States' and row['JobSatisfaction'] != 'NA' and row['Salary'] != 'NA':
            if float(row['Salary'])> 10000 and float(row['Salary']) <= 30000:
                regionBySatisfyByMoney[1][int(row['JobSatisfaction'])] += 1
            elif float(row['Salary']) > 30000 and float(row['Salary']) <= 50000:
                regionBySatisfyByMoney[2][int(row['JobSatisfaction'])] += 1
            elif float(row['Salary']) > 50000 and float(row['Salary']) <= 70000:
                regionBySatisfyByMoney[3][int(row['JobSatisfaction'])] +=1
            elif float(row['Salary']) > 70000 and float(row['Salary']) <= 90000:
                regionBySatisfyByMoney[4][int(row['JobSatisfaction'])] +=1
            elif float(row['Salary']) > 90000 and float(row['Salary']) <= 110000:
                regionBySatisfyByMoney[5][int(row['JobSatisfaction'])] +=1
            elif float(row['Salary']) > 110000:
                regionBySatisfyByMoney[6][int(row['JobSatisfaction'])] +=1
            else:
                regionBySatisfyByMoney[0][int(row['JobSatisfaction'])] +=1
print regionBySatisfyByMoney
