
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
categories = ['Recruiting', 'Onboarding', 'Training', 'Employee Engagement', 'Performance Management', 'Compensation and Benefits'] 
percentage = [25, 20, 20, 15, 10, 10]

plt.pie(percentage, labels=categories, startangle=90, autopct='%.1f%%', rotatelabels=True, textprops={'fontsize': 14, 'wrap':True})
plt.title('Employee Management Categories for Organizations in 2021', fontsize=16)
plt.tight_layout()
plt.savefig('pie chart/png/423.png')
plt.clf()