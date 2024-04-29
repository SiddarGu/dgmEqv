
import matplotlib.pyplot as plt
import numpy as np

data = [[2020,180000,1800],[2021,200000,2000],[2022,220000,2200],[2023,240000,2400]]

Year, Average_Home_Price, Average_Rent_Price = np.array(data).T

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

plt.bar(Year-0.2, Average_Home_Price, width=0.2, color='#F08080', label='Average Home Price')
plt.bar(Year, Average_Rent_Price, width=0.2, color='#87CEFA', label='Average Rent Price')

ax.set_xticks(Year)
ax.set_title('Average Home Price and Average Rent Price from 2020 to 2023', fontsize=15)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Price ($)', fontsize=15)

plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/216.png')
plt.show()
plt.clf()