
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
subplot = fig.add_subplot()

labels = ['Male', 'Female']
sizes = [45, 55]
colors = ['#00BFFF', '#FF1493']
explode = (0.05, 0)

subplot.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
subplot.set_title('Gender Distribution in the United States, 2023', fontsize=15)
plt.legend(labels, loc="best", bbox_to_anchor=(1, 0.5), fontsize=15)
plt.tight_layout()
plt.xticks(rotation=90)

plt.savefig('pie chart/png/278.png', bbox_inches='tight')

plt.clf()