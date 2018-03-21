import csv
import numpy as np
from scipy import stats

salary = []
with open('SalaryData.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='excel', delimiter=',' )
    for row in reader:
        salary.append(row)
        
salary_1 = np.array(salary)
total_exp = []
sal = []
exp = []
for i in range(1,53):
    exp.append(float(salary_1[i][2]))
    total_exp.append(float(salary_1[i][4]))
    sal.append(float(salary_1[i][5]))
exp1 = np.array(exp)    
print(exp1)    
median = np.median(exp1)
print(median)
mean = np.mean(exp1)
print(mean)

        
