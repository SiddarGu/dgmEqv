
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(1,1,1)

#Data
year = np.array([2019,2020,2021,2022,2023])
revenue = np.array([3000,4000,5000,6000,7000])
expense = np.array([2500,3000,3500,4000,4500])
profit = np.array([500,1000,1500,2000,2500])

#Plot
ax.plot(year, revenue, color='#A94FCF', linestyle='dashed', marker='o', label='Revenue')
ax.plot(year, expense, color='#F7D85D', linestyle='dashed', marker='o', label='Expense')
ax.plot(year, profit, color='#76D4DA', linestyle='dashed', marker='o', label='Profit')

#Setting xticks
plt.xticks(year)

#Setting title
ax.set_title('Financial performance of ABC Company from 2019 to 2023')

#Label data point
for a,b,c,d in zip(year,revenue,expense,profit):
    plt.annotate(f'Revenue:{b}\nExpense:{c}\nProfit:{d}',xy=(a,b),rotation=-45)

#Set legend
ax.legend(loc='upper left')

#Resize
plt.tight_layout()

#Save
plt.savefig('line chart/png/303.png')

#Clear
plt.clf()