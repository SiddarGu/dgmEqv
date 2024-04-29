
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig = plt.figure(figsize=(15, 8))
ax1 = fig.add_subplot()

# Data
education = ["Pre-K", "K-12", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate Degree"]
percentage = [5, 35, 10, 20, 15, 15]

# Plot
ax1.pie(percentage, labels=education, autopct='%1.1f%%', textprops={'wrap':True, 'rotation':90})
ax1.set_title("Education Level Distribution in the USA, 2023")

# Axis
ax1.xaxis.set_ticks_position('none')
ax1.yaxis.set_ticks_position('none')

# Resize figure
plt.tight_layout()

# Save and clear
plt.savefig("pie chart/png/415.png")
plt.clf()