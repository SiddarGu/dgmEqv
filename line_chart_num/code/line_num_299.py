
import matplotlib.pyplot as plt
import numpy as np

data = [[1000,10], [1200,12], [1400,14], [1600,16], [1800,20]]

fig, ax = plt.subplots(figsize=(12,6))
ax.set_title("Student Enrollment and Dropout Rate in Higher Education Institutions from 2020 to 2022")
ax.plot(data, marker='o', linewidth=2)
ax.set_xticks(np.arange(len(data)))
ax.set_xticklabels(['Fall 2020','Spring 2021','Fall 2021','Spring 2022','Fall 2022'])
ax.set_ylabel("Students(thousands)")
ax.set_xlabel("Semester")
ax.legend(["Enrollment","Dropout Rate"])

for i,j in enumerate(data):
    ax.annotate(str(j[1])+"%",xy=(i,j[1]),ha='center')

plt.tight_layout()
plt.savefig('line chart/png/501.png')
plt.clf()