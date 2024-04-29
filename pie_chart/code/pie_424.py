
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
gender_data = [40, 60]
labels = ['Male', 'Female']
ax.pie(gender_data, labels=labels, autopct='%.2f%%', textprops={'fontsize': 10},
       wedgeprops={'linewidth': 2, 'edgecolor': 'black'},
       startangle=90, shadow=True)
ax.axis('equal')
plt.title("Gender Distribution in Healthcare Services in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig('pie chart/png/387.png')
plt.clf()