
import matplotlib.pyplot as plt

plt.figure(figsize=(9,5))
ax = plt.subplot()
ax.bar(['USA', 'UK', 'Germany', 'France'], [21, 3, 4.5, 6], label='GDP(thousand billion)', width=0.6)
ax.bar(['USA', 'UK', 'Germany', 'France'], [2.4, 1.6, 1.1, 1.5], label='Inflation Rate', bottom=[21, 3, 4.5, 6], width=0.6)
ax.legend(loc='upper center')
plt.title('GDP and Inflation Rate of Four Countries in 2021')
plt.xticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar_395.png')
plt.clf()