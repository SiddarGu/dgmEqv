
import matplotlib.pyplot as plt
import numpy as np

causes = ["Education", "Healthcare", "Human Rights", "Environment", "Poverty Alleviation"]
percentages = [20, 25, 15, 20, 20]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(percentages, labels=causes, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})
ax.axis('equal') 
plt.title("Distribution of Charitable Causes in the United States, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/283.png")
plt.xticks(rotation=45)
plt.show()
plt.clf()