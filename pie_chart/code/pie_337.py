
import matplotlib.pyplot as plt
import numpy as np

# data
education_level = ["High School", "Associates Degree", "Bachelor's Degree", "Master's Degree", "Doctorate"]
percentage = [23, 15, 30, 20, 12]

# Bar Chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=education_level, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=90)
ax.axis('equal')
ax.set_title('Education Level Distribution among Adults in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/427.png')
plt.clf()