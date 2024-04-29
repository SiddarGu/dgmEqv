

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

fig = plt.figure(figsize=(20,10))

ax = fig.add_subplot(111)

education_level = ["High School","Associate Degree","Bachelor's Degree","Master's Degree","Doctoral Degree"]
percentage = [20,25,30,15,10]

ax.pie(percentage, labels=education_level, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 14, 'wrap': True, 'rotation': 0})

ax.set_title("Education Level Distribution in the United States, 2023", fontsize=24, fontweight='bold')
ax.axis('equal')
ax.legend(loc="best", fontsize=14)

plt.tight_layout()
fig.savefig('pie chart/png/229.png')

plt.clf()