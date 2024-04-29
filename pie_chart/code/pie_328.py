
import matplotlib.pyplot as plt

labels = ['Job Satisfaction','Professional Development','Compensation and Benefits','Work Environment','Work-Life Balance']
sizes = [35,25,20,15,5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffcccc']
explode = (0.1, 0.1, 0.1, 0.1, 0.1) 

plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
plt.axis('equal') 
plt.tight_layout()
plt.title("Employee Retention Factors in the Workplace, 2023")
plt.savefig('pie chart/png/104.png')
plt.show()
plt.clf()