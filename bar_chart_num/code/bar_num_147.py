
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 500, 100], ['UK', 600, 110], ['Germany', 550, 120], ['France', 580, 115]]

# Set figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()

# Set bar variables
country = [country[0] for country in data]
students = [country[1] for country in data]
teachers = [country[2] for country in data]

# Plot bars
ax.bar(country, students, label='Students', bottom=teachers, width=0.5)
ax.bar(country, teachers, label='Teachers', width=0.5)

# Set labels
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.set_title('Number of students and teachers in four countries in 2021')
ax.set_xticks(country)

# Set legend
ax.legend()

# Label value of each data point for every variables directly on the figure
for i in range(len(country)):
    ax.annotate(str(students[i]), xy=(country[i], students[i]+teachers[i]/2))
    ax.annotate(str(teachers[i]), xy=(country[i], teachers[i]/2))

# Adjust the image
fig.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/483.png')

# Clear the current image state
plt.close()