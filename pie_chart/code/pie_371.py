
import matplotlib.pyplot as plt
import numpy as np

Platforms = ['Facebook','YouTube','Twitter','Instagram','LinkedIn','Other']
Percentage = [30,25,15,15,10,5]

plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.pie(Percentage, labels=Platforms,autopct='%.1f%%',startangle=90,textprops={'fontsize':10})
ax.axis('equal')
ax.set_title('Distribution of Social Platform Usage in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/358.png')
plt.cla()