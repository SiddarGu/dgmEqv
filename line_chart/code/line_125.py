
import matplotlib.pyplot as plt
import numpy as np

Year = [1996,1997,1998,1999,2000]
Average_Farm_Price = [63.4,59.2,62.8,56.5,63.7]
Price_of_Corn = [50.9,64.7,68.6,64.2,58.2]
Price_of_Wheat = [75.3,53.6,51.2,45.9,67.7]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
ax.plot(Year, Average_Farm_Price, label='Average Farm Price',linewidth=2, color='red')
ax.plot(Year, Price_of_Corn, label='Price of Corn',linewidth=2, color='green')
ax.plot(Year, Price_of_Wheat, label='Price of Wheat',linewidth=2, color='purple')

plt.xticks(np.arange(min(Year), max(Year)+1, 1.0))
ax.set_title('Prices of corn and wheat in relation to average farm price,1996-2000')
ax.legend(loc='best', fontsize='medium')
plt.tight_layout()
plt.savefig('line chart/png/322.png')
plt.clf()