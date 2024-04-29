
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

figure_1 = plt.figure(figsize=(8,6))

ax = figure_1.add_subplot(111)

labels = ['Administrative', 'Information Technology', 'Manufacturing', 'Sales', 'Human Resources', 'Education', 'Other']
sizes = [25, 20, 15, 15, 10, 10, 5]

ax.pie(sizes, labels=labels, autopct='%.2f%%', startangle=90, textprops={'fontsize': 10})
ax.legend(labels,loc='lower left', fontsize='large')
ax.set_title('Distribution of Job Categories in the US in 2023', fontsize=15)

ax.set_xticks([])

plt.tight_layout()

plt.savefig('pie chart/png/524.png')

plt.cla()