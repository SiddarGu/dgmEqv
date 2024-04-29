
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([2001, 2002, 2003, 2004, 2005]) 
y1 = np.array([400, 450, 500, 550, 600]) 
y2 = np.array([100, 120, 140, 160, 180]) 
y3 = np.array([1000, 1100, 1200, 1300, 1400]) 

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(x, y1, color='blue', linestyle='-', label="Research Grants (million dollars)")
ax.plot(x, y2, color='orange', linestyle='-', label="Research Output (articles)")
ax.plot(x, y3, color='green', linestyle='-', label="R&D Expenditure (billion dollars)")
ax.set_xticks(x)

ax.legend(loc='best', ncol=2, prop={'size': 10})
plt.title('Analysis of Research and Development Expenditure in the Science and Engineering Sector')
plt.tight_layout()
plt.savefig('line chart/png/521.png')
plt.clf()