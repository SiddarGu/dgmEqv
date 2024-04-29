
import matplotlib.pyplot as plt 
import numpy as np

#create figure
fig, ax = plt.subplots(figsize=(10,7))

#read data
grade_level = np.array(['5th Grade','6th Grade','7th Grade','8th Grade','9th Grade','10th Grade'])
reading_score = np.array([80,90,85,95,90,95])
math_score = np.array([90,85,80,95,85,90])
science_score = np.array([70,75,65,75,70,80])

#plot line chart
ax.plot(grade_level,reading_score, label='Reading') 
ax.plot(grade_level,math_score, label='Mathematics') 
ax.plot(grade_level,science_score, label='Science')

#set axis
ax.set_xlabel('Grade Level')
ax.set_ylabel('Score')

#set title
ax.set_title('Academic Progress of Students from 5th to 10th Grade')

#set xticks
ax.set_xticks(np.arange(6))
ax.set_xticklabels(grade_level, rotation=45, wrap=True)

#set legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

#auto resize figure
fig.tight_layout()

#save figure
plt.savefig('line chart/png/141.png')

#clear current image state
plt.clf()