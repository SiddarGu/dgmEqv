
import matplotlib.pyplot as plt
import numpy as np

#Set data
Year = np.array([2019, 2020, 2021, 2022])
Revenue = np.array([10000, 12000, 15000, 18000])
Expenses = np.array([8000, 9000, 10000, 12000])

#Plot chart
plt.figure(figsize=(10, 8))
plt.plot(Year, Revenue, label='Revenue')
plt.plot(Year, Expenses, label='Expenses')

#Set legend position and font size
plt.legend(loc='upper right', fontsize='large')
plt.xticks(Year)

#Add chart title
plt.title('Financial Performance of ABC Corporation over the Years')
plt.tight_layout()

#Save chart
plt.savefig('line chart/png/86.png')

#Clear state
plt.clf()