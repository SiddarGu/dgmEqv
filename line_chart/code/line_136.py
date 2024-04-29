
import matplotlib.pyplot as plt
import numpy as np

data = [[2001,100,90,80],[2002,120,70,60],[2003,80,90,110],[2004,150,120,140]]
Year, Profit_A, Profit_B, Profit_C = np.array(data).T

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(Year, Profit_A, label='Profit A(million dollars)', marker='o')
ax.plot(Year, Profit_B, label='Profit B(million dollars)', marker='o')
ax.plot(Year, Profit_C, label='Profit C(million dollars)', marker='o')
ax.set_title('Profits of three companies in the pharmaceutical industry from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Profit (million dollars)')
ax.set_xticks(Year)
ax.grid(True)
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/489.png')
plt.clf()