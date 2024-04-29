
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK','Germany','France']
Number_of_Students = [25000,18000,21000,20000]
Number_of_Schools = [1000, 800, 900, 1200]

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(country, Number_of_Students, label='Number of Students', width=0.5, bottom=Number_of_Schools)
ax.bar(country, Number_of_Schools, label='Number of Schools', width=0.5)

for x,y,z in zip(country,Number_of_Students,Number_of_Schools):
    ax.annotate(str(y), xy=(x, y/2+z/2), ha='center')
    ax.annotate(str(z), xy=(x, z/2), ha='center')

ax.set_title('Number of students and schools in four countries in 2021')
ax.set_xticks(country)
ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/597.png')
plt.clf()