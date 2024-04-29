
import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(2000, 2006) 
y1_data = [20, 25, 30, 35, 40, 50]
y2_data = [2, 3, 4, 5, 6, 7]
y3_data = [45, 50, 60, 70, 80, 90]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_title('Transportation usage in the US from 2000-2005')
ax.plot(x_data, y1_data, label="Air Travel(million passengers)", marker='o')
ax.plot(x_data, y2_data, label="Rail Travel(million passengers)", marker='o')
ax.plot(x_data, y3_data, label="Road Travel(million passengers)", marker='o')
ax.legend(loc=1)
ax.set_xticks(x_data)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line chart/png/223.png")
plt.clf()