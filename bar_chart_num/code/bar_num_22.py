
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[450,650],[400,750],[500,850],[420,800]])

Region = ["East","West","North","South"]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(Region, data[:,0], label="Tax Revenue(million)", color="red", bottom=data[:,1])
ax.bar(Region, data[:,1], label="Government Spending(million)",color="blue")
ax.set_title('Tax Revenue and Government Spending in four regions in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)

for i, value in enumerate(data.flatten()):
    ax.annotate(value, xy=(i//2, value), ha='center', va='center')

plt.xticks(Region)
plt.tight_layout()
plt.savefig('Bar Chart/png/545.png')
plt.clf()