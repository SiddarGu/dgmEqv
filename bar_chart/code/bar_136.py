
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()
Country = np.array(['USA', 'UK', 'Germany', 'France'])
Research_Grants = np.array([500, 400, 300, 450])
Scientists = np.array([1200, 1000, 800, 1100])
ax.bar(Country, Research_Grants, label='Research Grants')
ax.bar(Country, Scientists, label='Scientists', bottom=Research_Grants)
ax.set_title('Number of research grants and scientists in four countries in 2021')
ax.legend(loc='best')
plt.xticks(Country, rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/426.png')
plt.clf()