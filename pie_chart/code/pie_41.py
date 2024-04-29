
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

labels = ['18-24', '25-34', '35-44', '45-54','55-64']
percentages = [20, 35, 20, 15, 10]

fig = plt.figure(figsize=(8, 8))
gs = gridspec.GridSpec(1, 1)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_title('Age Distribution of Employees in the US, 2023')
ax1.pie(percentages, labels=labels, autopct='%.2f%%',textprops={'fontsize': 12},startangle=90, shadow=True,wedgeprops={'linewidth': 1, 'edgecolor':"black"})

plt.savefig('pie chart/png/372.png', format='png')
plt.tight_layout()
plt.xticks([])
plt.show()
plt.clf()