
import matplotlib.pyplot as plt
import numpy as np

data = {'Primary':25, 'Secondary':35, 'High School':15, 'University':20, 'Postgraduate':5}

plt.figure(figsize=(10,10))

labels = list(data.keys())
values = list(data.values())

plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title('Level of Education Distribution in the USA, 2023')
plt.xticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('pie chart/png/431.png')
plt.clf()