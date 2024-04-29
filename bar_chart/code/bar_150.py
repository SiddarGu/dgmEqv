
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
ax = plt.subplot()
ax.bar(['North', 'South', 'East', 'West'], [1000, 900, 1200, 1100], label='Restaurants', color='green')
ax.bar(['North', 'South', 'East', 'West'], [4500, 4800, 4600, 4900], label='Customers', bottom=[1000, 900, 1200, 1100], color='orange')
plt.xlabel('Region')
plt.xticks(rotation=45, wrap=True)
plt.ylabel('Number')
plt.title('Number of restaurants and customers in four regions in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/418.png')
plt.clf()