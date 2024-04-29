
import matplotlib.pyplot as plt
import numpy as np

Year = np.array([2001, 2002, 2003, 2004])
Unemployment_Rate = np.array([6.5, 5.8, 5.2, 4.7])
Tax_Rate = np.array([35, 38, 41, 45])
Inflation_Rate = np.array([2.3, 2.5, 2.7, 2.9])
GDP_Growth_Rate = np.array([3.7, 5.7, 4.5, 3.2])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()
ax.plot(Year, Unemployment_Rate, marker='s', color='red', linestyle='--', linewidth=2, label='Unemployment Rate')
ax.plot(Year, Tax_Rate, marker='o', color='blue', linestyle='-', linewidth=2, label='Tax Rate')
ax.plot(Year, Inflation_Rate, marker='D', color='green', linestyle=':', linewidth=2, label='Inflation Rate')
ax.plot(Year, GDP_Growth_Rate, marker='^', color='black', linestyle='-.', linewidth=2, label='GDP Growth Rate')
ax.set_xticks(Year)
ax.set_title('Economic Indicators in the United States from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Rate (%)')
ax.legend(loc='best', fontsize='large')
plt.tight_layout()
plt.savefig('line chart/png/545.png')
plt.clf()