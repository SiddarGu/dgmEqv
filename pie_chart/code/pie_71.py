
import matplotlib.pyplot as plt
import pandas as pd 

labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
sizes = [15, 20, 25, 20, 12, 8]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=90, wedgeprops={'linewidth': 2, 'edgecolor': 'white'}, shadow=True)
plt.title('Age Group Distribution in the United States Population, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/509.png')
plt.clf()