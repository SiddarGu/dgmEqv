
import matplotlib.pyplot as plt
import numpy as np

years = [2001,2002,2003,2004,2005]
GDP = [2.4,2.6,2.8,2.9,3.1]
Inflation_Rate = [2.3,2.5,2.7,2.9,3.2]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(1,1,1)

ax.plot(years,GDP,label='Quarterly GDP')
ax.plot(years,Inflation_Rate,label='Quarterly Inflation Rate')
ax.set_title('Economic Indicators in the United States from 2001 to 2005')
ax.set_xlabel('Years')
ax.set_ylabel('GDP & Inflation Rate')
ax.set_xticks(years)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/106.png')
plt.clf()