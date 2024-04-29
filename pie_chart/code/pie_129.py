
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

labels = ["Civil","Criminal","Administrative","Constitutional","Human Rights"]
values = [25,35,25,10,5]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.pie(values, labels=labels,autopct='%.2f%%', shadow=True)
ax.set_title("Types of Court Cases in the USA, 2023")
ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
ax.axis('equal')
fig.tight_layout()
plt.savefig('pie chart/png/267.png',bbox_inches='tight')
plt.clf()