
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Fields = ['Physics', 'Mathematics', 'Chemistry', 'Engineering', 'Biotechnology', 'Geology', 'Astronomy']
Percentage = [20, 15, 20, 25, 10, 7, 3]

# Plot
fig = plt.figure(figsize=(7,7))
plt.subplot()
plt.pie(Percentage, labels=Fields,autopct='%1.1f%%', startangle=90,textprops={'fontsize': 12, 'color': 'black'})
plt.title('Distribution of Science and Engineering Fields in Higher Education, 2023', fontsize=14)
plt.axis('equal')
plt.xticks([])
plt.tight_layout()
plt.savefig('pie chart/png/297.png')
plt.clf()