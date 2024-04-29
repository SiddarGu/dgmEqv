
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots(figsize=(10, 10))
source_data = np.array([25, 30, 20, 15, 10])
source_labels = ["Solar", "Wind", "Hydroelectric", "Nuclear", "Natural Gas"]

ax.pie(source_data, labels=source_labels, autopct='%.2f%%', shadow=True, startangle=90, wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
ax.set_title("Distribution of Renewable Energy Sources in the U.S. in 2023")

for label in ax.patches:
    label.set_picker(True)
ax.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/449.png")
plt.clf()