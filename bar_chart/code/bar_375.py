
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[250, 120, 210, 140], [220, 100, 190, 120]])

fig, ax = plt.subplots(figsize=(7, 6))
ax.bar(np.arange(4), data[0], width=0.4, label='Smartphone Owners (million)')
ax.bar(np.arange(4)+0.4, data[1], width=0.4, label='Internet Users (million)')
ax.set_xticks(np.arange(4)+0.2)
ax.set_xticklabels(('USA', 'UK', 'Germany', 'France'))
ax.set_title('Number of smartphone owners and internet users in four countries in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/355.png')
plt.clf()