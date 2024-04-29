
import matplotlib.pyplot as plt
import numpy as np

Fields = ['Physical Science', 'Mathematics', 'Engineering', 'Computer Science', 'Biology', 'Chemistry', 'Other']
Percentage = [22, 19, 22, 19, 8, 8, 2]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.pie(Percentage, labels=Fields, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})

ax.set_title('Distribution of Scientific Fields in the USA, 2023', fontsize=16)
plt.legend(bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('pie chart/png/220.png')
plt.clf()