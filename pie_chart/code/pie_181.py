
import matplotlib.pyplot as plt
import numpy as np

causes = ["Education", "Health", "Poverty Alleviation", "Environment", "Animal Welfare", "Disaster Relief"]
percentage = [30, 20, 15, 15, 10, 10]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=causes, autopct='%1.1f%%', textprops={'fontsize': 12, 'wrap': True, 'rotation': 0})
ax.set_title("Charitable Spending on Selected Causes in 2020")
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/505.png', dpi=100)
plt.clf()