

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
Country = ["USA","UK","Germany","France"]
Enrollment = [90, 92, 87, 89]
Graduation = [45, 48, 42, 50]
Graduation_rate = [25, 27, 30, 35]

x = np.arange(len(Country))
ax.bar(x, Enrollment, color='#F08080', label='High School Enrollment(%)')
ax.bar(x, Graduation, color='#FFA500', bottom=Enrollment, label='University Enrollment(%)')
ax.bar(x, Graduation_rate, color='#ADD8E6', bottom=np.array(Enrollment)+np.array(Graduation),label='Graduation Rate(%)')
ax.set_title('Enrollment and graduation rate in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), rotation = 0, fontsize=7,  ha='center', va='bottom')

plt.rcParams['figure.figsize'] = (7,4)
plt.tight_layout()
plt.savefig('Bar Chart/png/620.png', bbox_inches = 'tight')
plt.clf()