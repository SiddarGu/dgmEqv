
import matplotlib.pyplot as plt
import numpy as np

# set figure size and layout
fig = plt.figure(figsize=(7, 6))
plt.tight_layout()

# set labels and data
labels = ['Female', 'Male']
data = [50, 50]

# set pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution in the Workforce, 2023")

# save figure
plt.savefig('pie chart/png/255.png')

# clear figure
plt.clf()