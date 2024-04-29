
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.bar(['January', 'February', 'March', 'April'], [100, 90, 110, 80], width=0.2, bottom=0, label='Production A(units)')
ax.bar(['January', 'February', 'March', 'April'], [120, 130, 140, 150], width=0.2, bottom=0, label='Production B(units)', alpha=0.7)
ax.bar(['January', 'February', 'March', 'April'], [80, 110, 120, 140], width=0.2, bottom=0, label='Production C(units)', alpha=0.5)
plt.xticks(rotation=45, ha='right')
ax.set_title('Production output in three categories from January to April 2021')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/91.png')
plt.clf()