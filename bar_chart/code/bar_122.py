
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2019,2000,1800],[2020,2500,2000],[2021,2800,2200]])

X = np.arange(data.shape[0])

plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.bar(X + 0.00, data[:,1], color = 'b', width = 0.25, label='Income')
ax.bar(X + 0.25, data[:,2], color = 'g', width = 0.25, label='Expenses')
plt.xticks(X,data[:,0])
plt.xlabel("Year")
plt.ylabel("Million")
plt.title("Income and Expenses of a company from 2019 to 2021")
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/494.png')
plt.clf()