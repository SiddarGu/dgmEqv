
import matplotlib.pyplot as plt
import numpy as np

#set data
City = np.array(['New York','Los Angeles','Chicago','Houston'])
Median_House_Price = np.array([400000,500000,300000,350000])
Average_Rent = np.array([2500,3000,2000,1800])

#set figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

#plot
x = np.arange(len(City))
width = 0.35
p1 = ax.bar(x, Median_House_Price, width, color='green', bottom=Average_Rent)
p2 = ax.bar(x, Average_Rent, width, color='red')

#label
ax.set_xticks(x)
ax.set_xticklabels(City)
ax.set_title('Median house prices and average rent in four US cities in 2021')
ax.legend((p1[0], p2[0]), ('Median House Price', 'Average Rent'), loc='lower center')

#annotate
for Median_House_Price, Average_Rent in zip(p1, p2):
    h = Median_House_Price.get_height()
    ax.annotate('{}'.format(h),
                xy=(Median_House_Price.get_x() + Median_House_Price.get_width() / 2, h),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    h = Average_Rent.get_height()
    ax.annotate('{}'.format(h),
                xy=(Average_Rent.get_x() + Average_Rent.get_width() / 2, h),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

#save figure
plt.tight_layout()
plt.savefig('Bar Chart/png/64.png')
plt.clf()