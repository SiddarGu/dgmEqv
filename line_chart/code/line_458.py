
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(15,7))
ax=fig.add_subplot(111)

data=[[2019, 900, 1200, 2100],
      [2020, 1000, 1500, 2500],
      [2021, 1200, 1400, 2600],
      [2022, 1100, 1700, 2800],
      [2023, 1300, 1900, 3200]]

year=np.array(data)[:,0]
online_sales=np.array(data)[:,1]
retail_sales=np.array(data)[:,2]
total_sales=np.array(data)[:,3]

plt.plot(year, online_sales, color='green', label="Online Sales") 
plt.plot(year, retail_sales, color='orange', label="Retail Sales")
plt.plot(year, total_sales, color='blue', label="Total Sales")

ax.set_title("Comparison of Online and Retail Sales from 2019 to 2023")
ax.set_xlabel("Year")
ax.set_ylabel("Sales (billion dollars)")

ax.set_xticks(year)
ax.set_xticklabels(year, rotation=45, ha='right', va='top')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("line chart/png/471.png")
plt.clf()