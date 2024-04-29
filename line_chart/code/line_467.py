
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,8))
ax = plt.subplot()

x_data = np.array([2015,2016,2017,2018,2019,2020])
y1_data = np.array([500,750,800,900,1000,1150])
y2_data = np.array([100,150,190,200,220,250])

ax.plot(x_data, y1_data, color='#3399FF', linestyle='-', label='Number of Tourists')
ax.plot(x_data, y2_data, color='#FF3399', linestyle='-', label='Average Spend per Tourist(USD)')

ax.set_xticks(x_data)
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Tourist Activity in the Caribbean Islands from 2015 to 2020")
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(True, color='#999999', linestyle='-', linewidth=1)
plt.tight_layout()
plt.savefig("line chart/png/247.png")
plt.clf()