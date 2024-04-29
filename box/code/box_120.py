
import matplotlib.pyplot as plt 
import numpy as np 

data = [[50000,70000,80000,90000,110000], 
        [55000,75000,85000,95000,111000], 
        [60000,77000,87000,98000,115000], 
        [48000,72000,82000,91000,108000], 
        [52000,73000,83000,94000,109000]] 
outliers = [[], [140000], [12000, 150000], [130000], []]

fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(111) 
ax.boxplot(data, whis=1.5) 

for i, outlier in enumerate(outliers): 
    if outlier: 
        ax.plot(np.full(len(outlier), i+1), outlier, 'ro', alpha=0.6) 
ax.set_title('Salary Distribution of Employees in Human Resources and Employee Management (2021)') 
ax.set_xticklabels(['Employee ID 12345', 'Employee ID 23456', 'Employee ID 34567', 
                    'Employee ID 45678', 'Employee ID 56789'], rotation=45, fontsize=12, wrap=True) 
ax.set_ylabel('Salary (Dollars)', fontsize=12) 
ax.grid(alpha=0.4, linestyle='--') 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/23_202312251608.png') 
plt.clf()