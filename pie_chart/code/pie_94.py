
import matplotlib.pyplot as plt
import numpy as np

job_roles = ['Management', 'Human Resources', 'Accounting', 'Sales and Marketing', 'Software Development', 'Customer Service'] 
percentage = [20, 15, 15, 25, 10, 15]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.axis('equal')

wedges, texts = ax.pie(percentage, startangle=90, wedgeprops=dict(width=0.5))

ax.legend(wedges, job_roles, bbox_to_anchor=(1, 0.5))
plt.setp(texts, size=14, weight="bold")
plt.title("Distribution of Job Roles in the Modern Workforce, 2023")

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/114.png')
plt.clf()