
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
engineering_graduates = [20000,21000,18000,22000] 
science_graduates = [30000,27000,29000,25000]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.bar(country, engineering_graduates, width=0.35, label="Engineering Graduates", bottom=science_graduates)
ax.bar(country, science_graduates, width=0.35, label="Science Graduates")
ax.set_title("Number of engineering and science graduates in four countries in 2021")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=4)
plt.xticks(country, rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/140.png')
plt.clf()