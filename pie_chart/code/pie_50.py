
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))
data = ["Materials Science", "Computer Science", "Physics", "Mathematics", "Chemistry", "Mechanical Engineering", "Electrical Engineering"]
percentage = [20, 25, 15, 15, 15, 10, 10]

plt.pie(percentage, labels=data, startangle=90, autopct='%.1f%%',
        textprops={'fontsize': 10}, shadow=True, radius=1.2, center=(0, 0))
plt.title("Distribution of Research Areas in Science and Engineering, 2023", fontsize=15, y=1.08)
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig('pie chart/png/410.png')
plt.clf()