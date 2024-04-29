
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
grade = ['5th', '6th', '7th', '8th']
math = [85, 90, 95, 98]
science = [90, 95, 98, 99]
english = [80, 85, 90, 95]
x = range(len(grade))
ax = plt.subplot()
ax.bar(x, math, width = 0.2, label = 'Math', color = 'b', bottom = english)
ax.bar(x, science, width = 0.2, label = 'Science', color = 'r', bottom = [i+j for i,j in zip(english,math)])
ax.bar(x, english, width = 0.2, label = 'English', color = 'g')
ax.set_xticks(x)
ax.set_xticklabels(grade, fontsize='large')
plt.title('Academic performance in Math, Science and English for 5th to 8th grade')
plt.xlabel('Grade', fontsize='large')
plt.ylabel('Score (%)', fontsize='large')
plt.legend(loc='lower right', fontsize='large')
plt.tight_layout()
plt.savefig('bar chart/png/510.png')
plt.clf()