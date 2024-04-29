
import matplotlib.pyplot as plt
import numpy as np

age_group = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
percentage = [15, 20, 20, 20, 15, 10]

# create figure
fig = plt.figure(figsize=(7,7))

# plot pie chart
ax = fig.add_subplot(111)
ax.pie(percentage, labels=age_group, autopct='%1.1f%%', startangle=90,
        textprops={'fontsize': 10, 'color':'k'})

ax.set_title('Healthcare Utilization by Age in the USA, 2023')
ax.legend(labels=age_group, loc='lower left', bbox_to_anchor=(-0.1, -0.1), fontsize=10)

# adjust the layout
plt.tight_layout()

# save figure
plt.savefig('pie chart/png/323.png')

# clear the current image state
plt.clf()