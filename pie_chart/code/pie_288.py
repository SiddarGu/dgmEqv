
import matplotlib.pyplot as plt
import numpy as np

percentages = [20, 25, 25, 15, 15]
labels = ["Health Care", "Education", "Social Security", "Infrastructure", "National Defense"]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title("Breakdown of Public Spending in the USA, 2023")
ax.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/345.png')
plt.clf()