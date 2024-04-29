
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
ax = plt.subplot()
ax.bar(['USA', 'UK', 'Germany', 'France'], [30, 45, 38, 25], label='Start-ups', bottom=0)
ax.bar(['USA', 'UK', 'Germany', 'France'], [200, 230, 210, 190], label='Loans Approved', bottom=[30, 45, 38, 25])
ax.bar(['USA', 'UK', 'Germany', 'France'], [1000, 1200, 1050, 1100], label='Tax Revenue(billion)', bottom=[230, 275, 248, 215])
ax.set_title('Business and finance activity in four countries in 2021')
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], rotation=45, wrap=True)
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/369.png')
plt.clf()