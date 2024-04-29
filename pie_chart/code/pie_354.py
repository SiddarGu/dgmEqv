
import matplotlib.pyplot as plt
import numpy as np
 
labels = ["Graduate Degree", "Bachelor's Degree", "Associate Degree", "High School Diploma", "Less than High School Diploma"]
percentages = [45, 30, 15, 5, 5]

plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=labels, autopct="%.2f%%", textprops={'fontsize': 14}, wedgeprops={"edgecolor": "k", 'linewidth': 2})
plt.title("Education Level of Engineering Professionals in the USA, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/147.png")
plt.clf()