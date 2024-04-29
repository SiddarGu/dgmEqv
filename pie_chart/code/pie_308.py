
import matplotlib.pyplot as plt
import numpy as np

labels = ['Bachelor\'s Degree','Master\'s Degree','Doctoral Degree','Associate Degree','Certificate/Diploma']
percents = [42, 18, 29, 7, 4]
colors = ['green', 'red', 'blue', 'pink', 'yellow']

plt.figure(figsize=(8,8))
plt.pie(percents, labels=labels, colors=colors, autopct='%.2f%%', shadow=True, startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
plt.legend(labels, loc='upper right', bbox_to_anchor=(1.2, 1))
plt.title('Distribution of Higher Education Degrees in the US, 2023', fontsize=14)
plt.tight_layout()
plt.savefig('pie chart/png/440.png', dpi=440)
plt.clf()