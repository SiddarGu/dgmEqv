
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))
labels = ["Senior Management","Mid Management","Entry Level","Interns","Part-Time Employees"]
sizes = [20,30,20,15,15]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0.1,0.1,0.1,0.1,0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Employee Distribution in a Company, 2023')
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/64.png')
plt.show()
plt.close()