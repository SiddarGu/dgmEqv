

import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
sizes = [20, 25, 20, 15, 10, 10]

ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={'linewidth': 2, 'edgecolor':'black'})
ax.set_title("Age Distribution of US Population in 2023")

plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/19.png')
plt.clf()