
import matplotlib.pyplot as plt
import numpy as np

labels = ['Facebook','Instagram','Twitter','YouTube','Snapchat','TikTok']
sizes = [25,20,15,20,10,10]

plt.figure(figsize=(10,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, 
        wedgeprops={'linewidth': 2}, textprops={'fontsize':14,'wrap': True})
plt.title("Social Media Usage in the US, 2023", fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/450.png')
plt.clf()