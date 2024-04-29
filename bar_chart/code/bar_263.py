
import matplotlib.pyplot as plt
import numpy as np

data = [['Harvard',5,10],['Stanford',7,12],['Cambridge',4,9],['Oxford',1,15]]

school, enrollment, student_teacher_ratio = zip(*data)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.bar(school, enrollment, width=0.5, label='Enrollment(hundred)')
ax.bar(school, student_teacher_ratio, width=0.2, bottom=enrollment, label='Student/Teacher Ratio(%)')

ax.set_title('Enrollment and student/teacher ratio of four renowned universities in 2021')
ax.set_ylabel('Number')
ax.set_xticklabels(school, rotation=45, ha='right')

ax.legend()
plt.tight_layout()
plt.savefig('bar_263.png')
plt.clf()