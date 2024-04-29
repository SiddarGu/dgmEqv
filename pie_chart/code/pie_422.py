
import matplotlib.pyplot as plt

fields = ['Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Computer Science', 'Chemical Engineering', 'Biomedical Engineering', 'Aerospace Engineering', 'Materials Science']
percentages = [20, 15, 15, 20, 15, 10, 5, 10]

fig = plt.figure(figsize=(10, 10), dpi=100)
ax = fig.add_subplot(111)

ax.pie(percentages, labels=fields, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Science and Engineering Fields in Higher Education, 2023')
plt.tight_layout()
plt.savefig("pie chart/png/218.png")
plt.clf()