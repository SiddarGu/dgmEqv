
import matplotlib.pyplot as plt
import numpy as np

#set data
grade = np.array(['Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3'])
score = np.array([85, 90, 92, 94])
students = np.array([1000, 900, 800, 700])

#initialize the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

#plot the data
ax.bar(grade, score, label='Average Score', bottom=0)
ax.bar(grade, students, label='Student Number', bottom=0)

#generate labels
for i in range(len(grade)):
    ax.text(x=i, y= score[i]/2 + students[i]/2, s=score[i], fontsize=12, ha='center', va='center')
    ax.text(x=i, y= students[i]/2, s=students[i], fontsize=12, va='center', ha='center')

#set the title
ax.set_title('Average score and student numbers of kindergarten to grade 3 in 2021')

#set the legend
ax.legend(loc='best')

#adjust the figure 
plt.xticks(grade)
plt.tight_layout()

#save the figure
plt.savefig('Bar Chart/png/541.png')

#clear the figure state
plt.clf()