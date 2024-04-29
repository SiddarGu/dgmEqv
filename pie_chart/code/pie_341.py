

import matplotlib.pyplot as plt
import numpy as np
 
# Data to plot
labels = 'Automotive', 'Aerospace', 'Electronics', 'Heavy Machinery', 'Food & Beverage', 'Pharmaceuticals', 'Textile', 'Other'
sizes = [20, 15, 15, 15, 15, 10, 10, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#d9b38c','#c2c2f0','#ffb3e6','#7f7f7f']

# Plot
fig1, ax1 = plt.subplots(figsize=(7,7))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.title('Manufacturing Industry Distribution in the USA, 2023')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/40.png')
plt.clf()