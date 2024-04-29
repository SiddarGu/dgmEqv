
import matplotlib.pyplot as plt
import numpy as np

#Creation of data
country = ['USA','UK','Germany','France']
students_enrolled = [50,40,30,35]
schools = [4000,3000,2500,3500]

#Create figure
fig, ax = plt.subplots(figsize=(12, 6))

#Plotting of data
ax.bar(country, students_enrolled, label='Enrolled Students', zorder=2)
ax.bar(country, schools, bottom=students_enrolled, label='Schools', zorder=2)

#Labeling of data
ax.set_title('Number of students enrolled and schools in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend(loc='upper left')
ax.set_xticks(country)

#Annotation of data
for i, v in enumerate(students_enrolled):
    ax.text(i-.1, v+2, str(v), color='black', fontweight='bold')
for i, v in enumerate(schools):
    ax.text(i-.1, v+2, str(v), color='black', fontweight='bold')

#Adjusting the display
plt.tight_layout()

#Save figure
plt.savefig('Bar Chart/png/451.png')

#Clear the current image state
plt.clf()