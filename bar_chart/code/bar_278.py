
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

#data
age_groups = ['10-20','21-30','31-40','41-50']
astronomy_knowledge = [10,14,20,17]
chemistry_knowledge = [8,11,13,15]
physics_knowledge = [7,10,14,11]

#plot
width = 0.2
x = np.arange(len(age_groups))
ax.bar(x, astronomy_knowledge, width=width, label='Astronomy Knowledge')
ax.bar(x + width, chemistry_knowledge, width=width, label='Chemistry Knowledge')
ax.bar(x + width*2, physics_knowledge, width=width, label='Physics Knowledge')

#labels
ax.set_title('Astronomy, Chemistry, and Physics Knowledge of Different Age Groups in 2021')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(age_groups, rotation=45, ha='right')
ax.set_ylabel('Knowledge')
ax.legend()

#tight layout
plt.tight_layout()

#save
plt.savefig('bar chart/png/191.png')

#reset
plt.clf()