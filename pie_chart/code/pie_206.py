
import matplotlib.pyplot as plt 
import numpy as np

#Create figure 
fig = plt.figure(figsize=(10,5))

# Define Data
labels = ["Grains","Pulses","Vegetables","Fruits","Oilseeds"]
sizes = [35,20,25,10,10]

# Define colors
colors = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd"]

# Plot pie chart
plt.pie(sizes, labels=labels, colors=colors,shadow=True,startangle=90, autopct='%1.1f%%')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Add Title
plt.title("Crop Distribution in India, 2023")

# Save Figure
plt.tight_layout()
plt.savefig("pie chart/png/80.png")

# Clear Figure
plt.clf()