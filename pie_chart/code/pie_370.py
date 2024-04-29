
import matplotlib.pyplot as plt
import numpy as np

labels = ['Full-Time', 'Part-Time', 'Contract', 'Interns', 'Freelancers']
values = [60, 20, 10, 5, 5]

plt.figure(figsize=(10, 10))
plt.pie(values, labels=labels, autopct='%1.1f%%',textprops={'fontsize': 14}, startangle=90)
plt.title("Employee Distribution in the US Workforce, 2023", fontsize=20, wrap=True)
plt.axis('equal')
plt.legend(loc="upper right", prop={'size': 16})
plt.tight_layout()
plt.savefig('pie chart/png/136.png')
plt.clf()